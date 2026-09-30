import { Maximize2, Minimize2, createElement } from 'lucide';

const KEYBOARD_RESIZE_PIXELS = 10;
const PROPERTIES = { explorer: '--explorer-width', guide: '--guide-width', questions: '--questions-height', code: '--code-height' };

export function clampPanelSize(size, minimum, available) {
  const maximum = Math.max(0, available);
  return Math.max(Math.min(minimum, maximum), Math.min(size, maximum));
}

export function setupPanelLayout(ui) {
  const workspace = document.querySelector('.workspace');
  const explorer = document.querySelector('.explorer');
  const code = document.querySelector('.code-pane');
  const guide = document.querySelector('.guide-pane');
  const lesson = document.querySelector('.guide-scroll');
  const questions = document.querySelector('.questions');
  const mobile = matchMedia('(max-width: 620px)');
  const compact = matchMedia('(max-width: 850px)');
  let sizes = {};
  try {
    const saved = JSON.parse(localStorage.getItem('guided-layout') || '{}');
    for (const key of Object.keys(PROPERTIES)) {
      if (Number.isFinite(saved?.[key]) && saved[key] > 0) {
        sizes[key] = saved[key];
        workspace.style.setProperty(PROPERTIES[key], `${saved[key]}px`);
      }
    }
  } catch { /* The layout remains adjustable without browser storage. */ }

  function persist() {
    try { localStorage.setItem('guided-layout', JSON.stringify(sizes)); }
    catch { /* Keep the current layout when storage is unavailable. */ }
  }

  function setSize(key, size) {
    if (sizes[key] === size) return;
    sizes[key] = size;
    workspace.style.setProperty(PROPERTIES[key], `${size}px`);
  }

  function columnLimits(key) {
    const style = getComputedStyle(workspace);
    const minimumCode = parseFloat(style.getPropertyValue('--code-min-width'));
    const minimumExplorer = parseFloat(style.getPropertyValue('--explorer-min-width'));
    const minimumGuide = parseFloat(style.getPropertyValue('--guide-min-width'));
    const divider = ui['guide-splitter'].getBoundingClientRect().width;
    const leftWidth = compact.matches ? 0 : explorer.getBoundingClientRect().width + ui['explorer-splitter'].getBoundingClientRect().width;
    const width = workspace.getBoundingClientRect().width;
    return key === 'explorer'
      ? { minimum: minimumExplorer, maximum: width - divider * 2 - minimumCode - minimumGuide }
      : { minimum: minimumGuide, maximum: width - leftWidth - divider - minimumCode };
  }

  function questionsLimits() {
    const style = getComputedStyle(lesson);
    const minimumLesson = parseFloat(style.paddingTop) + parseFloat(style.paddingBottom)
      + document.querySelector('.step-top').getBoundingClientRect().height
      + ui['step-title'].getBoundingClientRect().height;
    return {
      minimum: document.querySelector('.questions-heading').getBoundingClientRect().height + ui['question-form'].getBoundingClientRect().height,
      maximum: guide.getBoundingClientRect().height - minimumLesson - ui['questions-splitter'].getBoundingClientRect().height,
    };
  }

  function resize(key, requested) {
    if (key === 'guide' && mobile.matches) {
      const minimum = document.querySelector('.code-heading').getBoundingClientRect().height + document.querySelector('.code-footer').getBoundingClientRect().height;
      const formHeight = document.querySelector('.questions-heading').getBoundingClientRect().height + ui['question-form'].getBoundingClientRect().height;
      setSize('code', clampPanelSize(requested, minimum, workspace.getBoundingClientRect().height - formHeight - ui['guide-splitter'].getBoundingClientRect().height));
      return;
    }
    const limits = key === 'questions' ? questionsLimits() : columnLimits(key);
    setSize(key, clampPanelSize(requested, limits.minimum, limits.maximum));
  }

  function bindSplitter(key, handle, axis, direction, measure) {
    let drag = null;
    handle.addEventListener('pointerdown', event => {
      if (event.button !== 0) return;
      const coordinate = axis();
      drag = { coordinate, origin: event[coordinate], size: measure() };
      handle.setPointerCapture(event.pointerId);
      document.body.classList.add('resizing-panels');
      event.preventDefault();
    });
    handle.addEventListener('pointermove', event => {
      if (drag) resize(key, drag.size + (event[drag.coordinate] - drag.origin) * direction());
    });
    const release = () => {
      if (!drag) return;
      drag = null;
      document.body.classList.remove('resizing-panels');
      persist();
    };
    handle.addEventListener('pointerup', release);
    handle.addEventListener('pointercancel', release);
    handle.addEventListener('lostpointercapture', release);
    handle.addEventListener('keydown', event => {
      const arrows = axis() === 'clientX' ? ['ArrowLeft', 'ArrowRight'] : ['ArrowUp', 'ArrowDown'];
      if (!arrows.includes(event.key)) return;
      event.preventDefault();
      resize(key, measure() + (event.key === arrows[0] ? -1 : 1) * direction() * KEYBOARD_RESIZE_PIXELS);
      persist();
    });
    handle.addEventListener('dblclick', () => {
      const dimension = key === 'guide' && mobile.matches ? 'code' : key;
      delete sizes[dimension];
      workspace.style.removeProperty(PROPERTIES[dimension]);
      persist();
    });
  }

  bindSplitter('explorer', ui['explorer-splitter'], () => 'clientX', () => 1, () => explorer.getBoundingClientRect().width);
  bindSplitter('guide', ui['guide-splitter'], () => mobile.matches ? 'clientY' : 'clientX', () => mobile.matches ? 1 : -1, () => (mobile.matches ? code.getBoundingClientRect().height : guide.getBoundingClientRect().width));
  bindSplitter('questions', ui['questions-splitter'], () => 'clientY', () => -1, () => questions.getBoundingClientRect().height);

  ui['questions-expand'].append(createElement(Maximize2));
  ui['questions-expand'].addEventListener('click', () => {
    const expanded = guide.classList.toggle('questions-expanded');
    const label = expanded ? 'Riduci domande' : 'Espandi domande';
    ui['questions-expand'].setAttribute('aria-expanded', String(expanded));
    ui['questions-expand'].setAttribute('aria-label', label);
    ui['questions-expand'].title = label;
    ui['questions-expand'].replaceChildren(createElement(expanded ? Minimize2 : Maximize2));
  });

  function fit() {
    ui['guide-splitter'].setAttribute('aria-orientation', mobile.matches ? 'horizontal' : 'vertical');
    if (mobile.matches) {
      if (sizes.code) resize('guide', sizes.code);
    } else {
      if (!compact.matches && sizes.explorer) resize('explorer', sizes.explorer);
      if (sizes.guide) resize('guide', sizes.guide);
    }
    if (sizes.questions && !guide.classList.contains('questions-expanded')) resize('questions', sizes.questions);
  }
  new ResizeObserver(fit).observe(workspace);
  new ResizeObserver(fit).observe(guide);
  fit();
}
