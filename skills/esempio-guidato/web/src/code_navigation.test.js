import assert from 'node:assert/strict';
import { test } from 'node:test';
import { CodeNavigation, parseCodeLink } from './code_navigation.js';

test('code links select files and exact line ranges, without external paths', () => {
  assert.deepEqual(parseCodeLink('code:src/main.cpp#L285'), { path: 'src/main.cpp', startLine: 285, endLine: 285 });
  assert.deepEqual(parseCodeLink('code:src/my%20file.cpp#L20-L28'), { path: 'src/my file.cpp', startLine: 20, endLine: 28 });
  for (const target of ['https://example.com/#L1', 'code:../outside#L1', 'code:%2e%2e/outside#L1', 'code:/outside#L1', 'code:C:/outside#L1', 'code:src/main.cpp#L0', 'code:src/main.cpp#L28-L20']) {
    assert.equal(parseCodeLink(target), null, target);
  }
});

test('back and forward restore positions, and a new visit replaces forward history', () => {
  const history = new CodeNavigation();
  assert.equal(history.move(-1), null);
  history.visit({ path: 'a.cpp' }, null);
  history.visit({ path: 'b.cpp', startLine: 20 }, { top: 150, left: 30 });
  assert.equal(history.canGoBack, true);
  assert.deepEqual(history.move(-1, { top: 400, left: 0 }).position, { top: 150, left: 30 });
  assert.equal(history.canGoForward, true);
  assert.deepEqual(history.move(1, { top: 160, left: 35 }).position, { top: 400, left: 0 });
  history.move(-1, { top: 410, left: 0 });
  history.visit({ path: 'c.cpp' }, { top: 160, left: 35 });
  assert.equal(history.canGoForward, false);
  assert.deepEqual(history.entries.map(entry => entry.code.path), ['a.cpp', 'c.cpp']);
  assert.equal(history.move(1), null);
});
