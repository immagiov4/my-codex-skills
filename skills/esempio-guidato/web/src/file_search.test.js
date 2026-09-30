import assert from 'node:assert/strict';
import { test } from 'node:test';
import { rankFileMatches, visibleFileRange } from './file_search.js';

test('matching names are ordered by greatest query proportion, with stable path ties', () => {
  const files = ['z/sound_extra.cpp', 'b/sound.cpp', 'a/sound.cpp', 'sound.h', 'main.cpp'].map(path => {
    const name = path.split('/').pop();
    return { path, name, searchName: name.toLowerCase() };
  });
  assert.deepEqual(rankFileMatches(files, 'sound').map(file => file.path), ['sound.h', 'a/sound.cpp', 'b/sound.cpp', 'z/sound_extra.cpp']);
  assert.equal(rankFileMatches(files, 'missing').length, 0);
});

test('only rows intersecting the viewport are rendered, including partial rows', () => {
  assert.deepEqual(visibleFileRange(0, 100, 44, 563), { start: 0, end: 3 });
  assert.deepEqual(visibleFileRange(45, 100, 44, 563), { start: 1, end: 4 });
  assert.deepEqual(visibleFileRange(0, 100, 44, 2), { start: 0, end: 2 });
});
