import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdirSync, mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { discover, readWorktrees, writeInventory } from './worktree-inventory.mjs';

test('porcelain preserves spaces, lock flags and non-ASCII paths', () => {
  const rows = readWorktrees('worktree C:/local repo\0HEAD abc\0branch refs/heads/main\0\0worktree D:/prova è\0HEAD def\0detached\0locked\0\0');
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
