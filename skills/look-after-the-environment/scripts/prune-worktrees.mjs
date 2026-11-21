#!/usr/bin/env node
// Remove Git worktrees whose work is already safe elsewhere. Dry run unless --execute.
// A worktree qualifies only when: it is a linked worktree under --root, not locked, idle for
// --min-idle-days, has no uncommitted or untracked files, no process references its path, and
// its HEAD is on a remote or equals the head of a merged pull request (gh, when available).
// Usage: node prune-worktrees.mjs --repo <main checkout> --root <worktrees dir> [--min-idle-days 3] [--execute] [--log <file>]
import { execFileSync, spawnSync } from 'node:child_process';
import { appendFileSync, existsSync, mkdirSync, statSync, readFileSync } from 'node:fs';
import { dirname, resolve, sep } from 'node:path';
import { homedir } from 'node:os';

const args = process.argv.slice(2);
const opt = name => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : undefined; };
const repo = opt('--repo'), root = opt('--root');
if (!repo || !root) { console.error('Usage: prune-worktrees.mjs --repo <main checkout> --root <worktrees dir> [--min-idle-days 3] [--execute] [--log <file>]'); process.exit(2); }
const minIdleDays = Number(opt('--min-idle-days') ?? 3), execute = args.includes('--execute');
const logFile = opt('--log') ?? resolve(homedir(), '.look-after-the-environment', 'prune-worktrees.log');
mkdirSync(dirname(logFile), { recursive: true });
const log = entry => appendFileSync(logFile, JSON.stringify({ ts: new Date().toISOString(), repo, execute, ...entry }) + '\n');
const norm = p => resolve(p).toLowerCase().replaceAll('/', sep).replace(/[\\/]+$/, '');
const git = (cwd, ...a) => execFileSync('git', ['-C', cwd, ...a], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'], timeout: 120000 }).trim();

function processCommandLines() {
  const r = process.platform === 'win32'
    ? spawnSync('powershell.exe', ['-NoProfile', '-NonInteractive', '-Command', 'Get-CimInstance Win32_Process | ForEach-Object { $_.CommandLine }'], { encoding: 'utf8', windowsHide: true, timeout: 60000 })
    : spawnSync('ps', ['-eo', 'args='], { encoding: 'utf8', timeout: 60000 });
  if (r.status !== 0) throw new Error('cannot list processes; refusing to prune');
  return r.stdout.toLowerCase();
}
function mergedPrHeads() {
  const r = spawnSync('gh', ['pr', 'list', '--state', 'merged', '--limit', '500', '--json', 'headRefOid'], { cwd: repo, encoding: 'utf8', windowsHide: true, timeout: 120000 });
  if (r.status !== 0) return { heads: new Set(), available: false };
  return { heads: new Set(JSON.parse(r.stdout).map(p => p.headRefOid)), available: true };
}

try {
  const rootKey = norm(root), mainKey = norm(repo);
  const procs = processCommandLines(), merged = mergedPrHeads();
  const freeBefore = freeBytes(root);
  const blocks = git(repo, 'worktree', 'list', '--porcelain').split(/\n\n+/).map(b => Object.fromEntries(b.split('\n').map(l => { const i = l.indexOf(' '); return i < 0 ? [l, true] : [l.slice(0, i), l.slice(i + 1)]; })));
  const results = [];
  for (const w of blocks) {
    const path = w.worktree; if (!path) continue;
    const key = norm(path); if (key === mainKey || !key.startsWith(rootKey + sep)) continue;
    const reasons = [];
    if (w.locked) reasons.push('locked');
    if (!existsSync(path)) { reasons.push('missing-directory'); results.push({ path, keep: true, reasons }); continue; }
    const head = w.HEAD;
    let gitdir = null; try { gitdir = resolve(path, git(path, 'rev-parse', '--git-dir')); } catch { reasons.push('not-a-worktree'); }
    const times = [Date.parse(git(path, 'log', '-1', '--format=%cI') || 0)];
    if (gitdir && existsSync(resolve(gitdir, 'logs', 'HEAD'))) times.push(statSync(resolve(gitdir, 'logs', 'HEAD')).mtimeMs);
    const idleDays = (Date.now() - Math.max(...times)) / 864e5;
    if (idleDays < minIdleDays) reasons.push(`active-${idleDays.toFixed(1)}d`);
    if (git(path, 'status', '--porcelain', '--untracked-files=normal')) reasons.push('uncommitted-changes');
    const unique = Number(git(path, 'rev-list', '--count', 'HEAD', '--not', '--remotes'));
    if (unique > 0 && !merged.heads.has(head)) reasons.push(`unpublished-commits-${unique}`);
    if (procs.includes(key)) reasons.push('process-uses-path');
    results.push({ path, branch: w.branch ?? 'detached', idleDays: Number(idleDays.toFixed(1)), keep: reasons.length > 0, reasons });
  }
  let removed = 0, failed = 0;
  for (const r of results.filter(r => !r.keep)) {
    if (!execute) continue;
    const out = spawnSync('git', ['-c', 'core.longpaths=true', '-C', repo, 'worktree', 'remove', '--', r.path], { encoding: 'utf8', windowsHide: true, timeout: 600000 });
    r.removed = out.status === 0 && !existsSync(r.path);
    if (r.removed) removed++; else { failed++; r.error = (out.stderr || 'directory still present').trim().slice(0, 300); }
  }
  if (execute) git(repo, 'worktree', 'prune');
  const freeAfter = freeBytes(root);
  const summary = { candidates: results.filter(r => !r.keep).length, kept: results.filter(r => r.keep).length, removed, failed, mergedPrLookup: merged.available, freedBytes: freeAfter != null && freeBefore != null ? freeAfter - freeBefore : null };
  for (const r of results) log({ path: r.path, branch: r.branch, keep: r.keep, reasons: r.reasons, removed: r.removed, error: r.error });
  log({ summary });
  console.log(JSON.stringify({ summary, results }, null, 1));
  process.exitCode = failed ? 1 : 0;
} catch (error) { log({ failure: error.message }); console.error(error.message); process.exitCode = 1; }

function freeBytes(p) {
  try {
    if (process.platform === 'win32') { const drive = resolve(p).slice(0, 1); const r = spawnSync('powershell.exe', ['-NoProfile', '-NonInteractive', '-Command', `(Get-PSDrive ${drive}).Free`], { encoding: 'utf8', windowsHide: true, timeout: 30000 }); return Number(r.stdout.trim()); }
    return Number(spawnSync('df', ['-B1', '--output=avail', p], { encoding: 'utf8' }).stdout.trim().split('\n').pop());
  } catch { return null; }
}
