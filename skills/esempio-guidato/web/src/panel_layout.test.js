import assert from 'node:assert/strict';
import { test } from 'node:test';
import { clampPanelSize } from './panel_layout.js';

test('panels stay between their content minimum and the available space', () => {
  assert.equal(clampPanelSize(500, 330, 900), 500);
  assert.equal(clampPanelSize(200, 330, 900), 330);
  assert.equal(clampPanelSize(1200, 330, 900), 900);
  assert.equal(clampPanelSize(500, 330, 250), 250);
  assert.equal(clampPanelSize(500, 330, -10), 0);
});
