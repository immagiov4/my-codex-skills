import assert from 'node:assert/strict';

// Use with a cua_repl browser tab whose concept map is open.
export async function checkMapMouse(tab) {
  const readMap = () => tab.playwright.evaluate(() => {
    const svg = document.querySelector('#map-canvas svg');
    return {
      bounds: svg.getBoundingClientRect().toJSON(),
      matrix: svg.querySelector('.svg-pan-zoom_viewport').getAttribute('transform')
        .slice(7, -1).split(',').map(Number),
    };
  });
  const roundingTolerance = 0.01;
  const closeTo = (actual, expected) => assert.ok(Math.abs(actual - expected) < roundingTolerance,
    `Expected ${expected}, got ${actual}`);
  const before = await readMap();
  const center = [Math.round(before.bounds.x + before.bounds.width / 2),
    Math.round(before.bounds.y + before.bounds.height / 2)];
  const distance = [Math.round(before.bounds.width / 4), Math.round(before.bounds.height / 4)];
  try {
    await tab.scroll(center, 'up', 3);
    await tab.getAXState();
    const zoomed = await readMap();
    const ratio = zoomed.matrix[0] / before.matrix[0];
    assert.ok(ratio > 1, 'Mouse wheel must zoom in');
    const anchor = [center[0] - before.bounds.x, center[1] - before.bounds.y];
    closeTo(zoomed.matrix[4], anchor[0] - (anchor[0] - before.matrix[4]) * ratio);
    closeTo(zoomed.matrix[5], anchor[1] - (anchor[1] - before.matrix[5]) * ratio);
    await tab.drag(center, [center[0] + distance[0], center[1] + distance[1]]);
    await tab.getAXState();
    const dragged = await readMap();
    closeTo(dragged.matrix[0], zoomed.matrix[0]);
    closeTo(dragged.matrix[4] - zoomed.matrix[4], distance[0]);
    closeTo(dragged.matrix[5] - zoomed.matrix[5], distance[1]);
    return { wheelZoom: true, cursorAnchor: true, mouseDrag: true };
  } finally {
    await tab.playwright.getByRole('button', { name: 'Adatta alla finestra', exact: true }).click();
    await tab.getAXState();
  }
}
