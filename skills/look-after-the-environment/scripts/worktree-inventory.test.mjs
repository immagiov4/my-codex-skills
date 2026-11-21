import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { mkdirSync, mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { discover, inventory, readWorktrees, writeInventory } from './worktree-inventory.mjs';

test('porcelain preserves spaces, lock flags and non-ASCII paths', () => {
  const rows = readWorktrees('worktree C:/local repo\nHEAD abc\nbranch refs/heads/main\n\nworktree D:/prova è\nHEAD def\ndetached\nlocked\n\n');
  assert.equal(rows[0].worktree, 'C:/local repo');
  assert.equal(rows[1].worktree, 'D:/prova è');
  assert.equal(rows[1].locked, true);
});

test('discovery finds nested Git markers and identifies evidence folders once', () => {
  const root = mkdtempSync(join(tmpdir(), 'inventory-fixture-'));
  const repo = join(root, 'nested', 'repo');
  mkdirSync(join(repo, '.git'), { recursive: true });
  mkdirSync(join(repo, 'evidence-example'));
  mkdirSync(join(repo, 'node_modules', 'embedded', '.git'), { recursive: true });
  const errors = [];
  const result = discover([repo, root], errors);
  assert.equal(result.repositories.size, 1);
  assert.equal(result.leftovers.size, 1);
  assert.deepEqual(errors, []);
  const config = join(root, 'invalid.json');
  writeFileSync(config, JSON.stringify({ minIdleDays: 0 }));
  assert.throws(() => writeInventory(config), /at least 1.5/);
});

test('installed Windows Git registers a linked checkout in the inventory', { skip: process.platform !== 'win32' }, () => {
  const root = mkdtempSync(join(tmpdir(), 'inventory-fixture-'));
  const repo = join(root, 'main');
  const linked = join(root, 'linked checkout');
  mkdirSync(repo);
  const git = (...args) => execFileSync('git', ['-C', repo, ...args], { windowsHide: true, stdio: 'pipe' });
  git('init');
  git('-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.test', 'commit', '--allow-empty', '-m', 'Test inventory');
  git('worktree', 'add', '--detach', linked);
  const result = inventory({ repositoryRoots: [root], worktreeRoots: [], leftoverRoots: [], minIdleDays: 1.5 });
  assert.equal(result.repositories, 1);
  assert.equal(result.results.length, 1);
  assert.equal(result.results[0].path.replaceAll('\\', '/').toLowerCase(), linked.replaceAll('\\', '/').toLowerCase());
  assert.ok(result.results[0].reasons.includes('attività recente'));
  assert.ok(result.results[0].reasons.includes('pubblicazione da verificare'));
});
