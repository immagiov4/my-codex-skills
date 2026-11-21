import { spawnSync } from 'node:child_process';
import { lstatSync, readdirSync, readFileSync, realpathSync, writeFileSync } from 'node:fs';
import { basename, dirname, join, resolve } from 'node:path';

const key = path => resolve(path).replaceAll('\\', '/').toLowerCase();
const skip = new Set(['.git', 'node_modules', '.bun', '.venv', 'target', '__pycache__']);
const run = (command, args) => {
  const result = spawnSync(command, args, {
    encoding: 'utf8', windowsHide: true, timeout: 30000, maxBuffer: 16 * 1024 * 1024,
    env: { ...process.env, GIT_OPTIONAL_LOCKS: '0', GIT_TERMINAL_PROMPT: '0' },
  });
  if (result.status !== 0) throw new Error(result.error?.message ?? result.stderr.trim());
  return result.stdout.trimEnd();
};
const git = (path, ...args) => run('git', ['-c', 'core.longpaths=true', '-C', path, ...args]);

export function discover(roots, errors) {
  const repositories = new Map();
  const leftovers = new Map();
  const seen = new Set();
  function walk(path) {
    try {
      const canonical = realpathSync(path);
      if (seen.has(key(canonical))) return;
      seen.add(key(canonical));
      const entries = readdirSync(canonical, { withFileTypes: true });
      if (entries.some(entry => entry.name === '.git')) repositories.set(key(canonical), canonical);
      for (const entry of entries) {
        if (!entry.isDirectory() || skip.has(entry.name)) continue;
        const child = join(canonical, entry.name);
        if (/^(evidence-|gep-)/i.test(entry.name)) leftovers.set(key(child), child);
        walk(child);
      }
    } catch (error) { errors.push({ path, error: error.message }); }
  }
  for (const root of roots) walk(root);
  return { repositories, leftovers };
}

function measure(path) {
  let bytes = 0, dependencies = 0, sharedDependencies = 0, lastWrite = 0;
  const errors = [];
  function walk(directory, dependency = false) {
    try {
      for (const entry of readdirSync(directory, { withFileTypes: true })) {
        const child = join(directory, entry.name);
        const stat = lstatSync(child);
        lastWrite = Math.max(lastWrite, stat.mtimeMs);
        if (stat.isSymbolicLink()) continue;
        const inDependencies = dependency || entry.name === 'node_modules';
        if (stat.isDirectory()) walk(child, inDependencies);
        else if (stat.isFile()) {
          bytes += stat.size;
          if (inDependencies && stat.nlink === 1) dependencies += stat.size;
          if (inDependencies && stat.nlink > 1) sharedDependencies += stat.size;
        }
      }
    } catch (error) { errors.push(error.message); }
  }
  walk(path);
  return { bytes, dependencies, sharedDependencies, lastWrite, errors };
}

function liveRefs(repo) {
  const hashes = new Set();
  for (const remote of git(repo, 'remote').split(/\r?\n/).filter(Boolean)) {
    for (const line of git(repo, 'ls-remote', remote).split(/\r?\n/)) {
      if (line) hashes.add(line.split(/\s/)[0]);
    }
  }
  return hashes;
}

export function readWorktrees(porcelain) {
  return porcelain.split('\0\0').filter(Boolean).map(block =>
    Object.fromEntries(block.split('\0').filter(Boolean).map(line => {
      const space = line.indexOf(' ');
      return space < 0 ? [line, true] : [line.slice(0, space), line.slice(space + 1)];
    })));
}

export function inventory(config) {
  const errors = [];
  const roots = [...config.repositoryRoots, ...config.worktreeRoots];
  const { repositories, leftovers } = discover(roots, errors);
  for (const root of config.leftoverRoots) {
    try {
      for (const entry of readdirSync(root, { withFileTypes: true })) {
        if (entry.isDirectory() && /^(evidence-|gep-|codex-|claude-|t3-|worktree-)/i.test(entry.name)) {
          const path = join(root, entry.name);
          leftovers.set(key(path), path);
        }
      }
    } catch (error) { errors.push({ path: root, error: error.message }); }
  }
  const processes = run('powershell.exe', ['-NoProfile', '-NonInteractive', '-Command',
    '$ErrorActionPreference="Stop"; Get-CimInstance Win32_Process | ForEach-Object { $_.CommandLine; $_.ExecutablePath }'])
    .replaceAll('\\', '/').toLowerCase();
  const registered = new Map();
  const queried = new Set();
  for (const repo of repositories.values()) {
    try {
      const common = key(git(repo, 'rev-parse', '--path-format=absolute', '--git-common-dir'));
      if (queried.has(common)) continue;
      const trees = readWorktrees(git(repo, 'worktree', 'list', '--porcelain', '-z'));
      queried.add(common);
      for (const [index, tree] of trees.entries()) {
        if (index === 0) continue;
        registered.set(key(tree.worktree), { tree, repo: trees[0].worktree });
      }
    } catch (error) { errors.push({ path: repo, error: error.message }); }
  }
  const refs = new Map();
  const merged = new Map();
  const results = [];
  for (const [pathKey, { tree, repo }] of registered) {
    const path = tree.worktree;
    const row = { path, repo, branch: tree.branch ?? 'detached', head: tree.HEAD, reasons: [] };
    const keep = reason => row.reasons.push(reason);
    try {
      if (tree.locked !== undefined) keep('bloccata in Git');
      if (tree.prunable !== undefined) keep('registrazione Git da verificare');
      if (key(realpathSync(path)) !== pathKey) keep('percorso reindirizzato');
      Object.assign(row, measure(path));
      if (row.errors.length) keep('misura incompleta');
      const gitDir = git(path, 'rev-parse', '--absolute-git-dir');
      let reflog = 0;
      try { reflog = lstatSync(join(gitDir, 'logs', 'HEAD')).mtimeMs; }
      catch (error) { if (error.code !== 'ENOENT') throw error; }
      const last = Math.max(row.lastWrite, reflog, Date.parse(git(path, 'log', '-1', '--format=%cI')));
      row.lastActive = new Date(last).toISOString();
      row.idleDays = (Date.now() - last) / 86400000;
      if (row.idleDays < config.minIdleDays) keep('attività recente');
      row.changes = git(path, 'status', '--porcelain', '--untracked-files=all');
      if (row.changes) keep('modifiche locali');
      row.ignored = git(path, 'ls-files', '--others', '--ignored', '--exclude-standard', '--directory');
      if (row.ignored) keep('file ignorati da classificare');
      row.processReference = processes.includes(pathKey);
      if (row.processReference) keep('percorso citato da un processo');
      if (!refs.has(repo)) {
        try { refs.set(repo, liveRefs(repo)); }
        catch (error) { refs.set(repo, new Set()); errors.push({ path: repo, error: error.message }); }
      }
      const hashes = refs.get(repo);
      const ancestors = new Set(git(path, 'for-each-ref', '--contains', tree.HEAD, '--format=%(objectname)', 'refs/remotes').split(/\r?\n/));
      if (hashes.has(tree.HEAD) || [...ancestors].some(hash => hashes.has(hash))) row.publication = 'ref remoto verificato';
      else {
        if (!merged.has(repo)) {
          try {
            const prs = JSON.parse(run('gh', ['-R', git(repo, 'remote', 'get-url', 'origin'), 'pr', 'list', '--state', 'merged', '--limit', '500', '--json', 'headRefOid,number']));
            merged.set(repo, new Map(prs.map(pr => [pr.headRefOid, pr.number])));
          } catch { merged.set(repo, new Map()); }
        }
        const pr = merged.get(repo).get(tree.HEAD);
        if (pr) row.publication = 'HEAD del PR unito #' + pr;
        else {
          keep('pubblicazione da verificare');
          row.unpublished = git(path, 'log', '--format=%h %s', 'HEAD', '--not', '--remotes');
        }
      }
    } catch (error) { keep('verifica incompleta: ' + error.message); }
    results.push(row);
  }
  for (const root of config.worktreeRoots) {
    function collect(path, remaining) {
      if (registered.has(key(path)) || repositories.has(key(path))) return;
      try {
        const children = readdirSync(path, { withFileTypes: true }).filter(entry => entry.isDirectory());
        if (path !== root && (remaining <= 0 || children.length === 0)) {
          leftovers.set(key(path), path);
          return;
        }
        for (const child of children) collect(join(path, child.name), remaining - 1);
      } catch (error) { errors.push({ path, error: error.message }); }
    }
    collect(root, config.containerDepth?.[root] ?? 1);
  }
  for (const [pathKey, path] of leftovers) {
    if (registered.has(pathKey)) continue;
    const row = { path, ...measure(path), processReference: processes.includes(pathKey), reasons: ['cartella residua: riferimenti e dati da verificare'] };
    if (row.lastWrite) row.lastActive = new Date(row.lastWrite).toISOString();
    results.push(row);
  }
  return { timestamp: new Date().toISOString(), repositories: queried.size, results: results.sort((a, b) => a.path.localeCompare(b.path)), errors };
}

export function writeInventory(configPath) {
  const config = JSON.parse(readFileSync(configPath, 'utf8').replace(/^\uFEFF/, ''));
  if (!Number.isFinite(config.minIdleDays) || config.minIdleDays < 1.5) throw new Error('minIdleDays must be at least 1.5');
  const file = resolve(dirname(configPath), config.output ?? 'worktree-inventory.json');
  writeFileSync(file, JSON.stringify(inventory(config), null, 2) + '\n');
}
