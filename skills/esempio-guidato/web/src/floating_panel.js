const KEYBOARD_MOVE_PIXELS = 16;

export function makeFloatingPanel({ panel, handle, onPosition, onRelease }) {
  let drag = null;
  function place(position) {
    const bounds = panel.getBoundingClientRect();
    const x = Math.max(0, Math.min(position.x, innerWidth - bounds.width));
    const y = Math.max(0, Math.min(position.y, innerHeight - bounds.height));
    panel.style.left = `${x}px`;
    panel.style.top = `${y}px`;
    onPosition({ x, y });
  }
  handle.addEventListener('pointerdown', event => {
    if (event.button !== 0) return;
    const bounds = panel.getBoundingClientRect();
    drag = { x: event.clientX - bounds.x, y: event.clientY - bounds.y };
    handle.setPointerCapture(event.pointerId);
    event.preventDefault();
  });
  handle.addEventListener('pointermove', event => {
    if (drag) place({ x: event.clientX - drag.x, y: event.clientY - drag.y });
  });
  handle.addEventListener('pointerup', () => {
    if (drag) { drag = null; onRelease(); }
  });
  handle.addEventListener('pointercancel', () => { drag = null; });
  handle.addEventListener('keydown', event => {
    const offsets = { ArrowLeft: [-1, 0], ArrowRight: [1, 0], ArrowUp: [0, -1], ArrowDown: [0, 1] };
    if (!offsets[event.key]) return;
    event.preventDefault();
    const [x, y] = offsets[event.key];
    const bounds = panel.getBoundingClientRect();
    place({ x: bounds.x + x * KEYBOARD_MOVE_PIXELS, y: bounds.y + y * KEYBOARD_MOVE_PIXELS });
    onRelease();
  });
  window.addEventListener('resize', () => {
    if (!panel.hidden) {
      const bounds = panel.getBoundingClientRect();
      place({ x: bounds.x, y: bounds.y });
    }
  });
  return place;
}
