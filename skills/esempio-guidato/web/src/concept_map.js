import { Code, Download, GripHorizontal, Maximize2, Minimize2, Network, Scan, X, ZoomIn, ZoomOut, createElement } from 'lucide';
import DOMPurify from 'dompurify';
import { makeFloatingPanel } from './floating_panel.js';

const ZOOM_FACTOR = 1.25;
let renderId = 0;
let renderQueue = Promise.resolve();

export function setupConceptMap(ui, projectName) {
  const panel = ui['concept-map'];
  const canvas = ui['map-canvas'];
  const viewport = ui['map-viewport'];
  for (const [id, icon] of [['map-toggle', Network], ['map-export', Download], ['map-grip', GripHorizontal], ['map-close', X], ['map-expand', Maximize2], ['map-source-toggle', Code], ['map-fit', Scan], ['map-zoom-in', ZoomIn], ['map-zoom-out', ZoomOut]]) {
    ui[id].append(createElement(icon));
  }
  let diagram = null;
  let renderedKey = null;
  let requestedKey = null;
  let scale = 1;
  let position = null;
  try { position = JSON.parse(localStorage.getItem('guided-map-position')); }
  catch { /* The panel remains movable without saved positioning. */ }
  const place = makeFloatingPanel({
    panel, handle: ui['map-drag'],
    onPosition: next => { position = next; },
    onRelease: () => {
      try { localStorage.setItem('guided-map-position', JSON.stringify(position)); }
      catch { /* Positioning also works for the current page without storage. */ }
    },
  });

  function zoom(nextScale) {
    const svg = canvas.querySelector('svg');
    if (!svg) return;
    scale = nextScale;
    const box = svg.viewBox.baseVal;
    svg.style.width = `${box.width * scale}px`;
    svg.style.height = `${box.height * scale}px`;
  }

  function fit() {
    const svg = canvas.querySelector('svg');
    if (!svg || viewport.hidden) return;
    const box = svg.viewBox.baseVal;
    const padding = parseFloat(getComputedStyle(viewport).padding) * 2;
    zoom(Math.min((viewport.clientWidth - padding) / box.width, (viewport.clientHeight - padding) / box.height));
  }

  function render() {
    if (panel.hidden) return;
    if (!diagram) {
      ui['map-status'].textContent = 'Mappa in preparazione';
      return;
    }
    const dark = document.documentElement.dataset.theme === 'dark';
    const key = `${diagram.revision}:${dark}`;
    if (key === renderedKey || key === requestedKey) return;
    const source = diagram.source;
    requestedKey = key;
    ui['map-status'].textContent = 'Disegno...';
    const draw = async () => {
      const { default: mermaid } = await import('mermaid');
      const colors = getComputedStyle(document.documentElement);
      mermaid.initialize({
        securityLevel: 'strict', startOnLoad: false, htmlLabels: false, theme: 'base', fontFamily: 'Segoe UI, sans-serif',
        themeVariables: {
          darkMode: dark, primaryColor: colors.getPropertyValue('--raised').trim(), primaryTextColor: colors.getPropertyValue('--text').trim(),
          primaryBorderColor: colors.getPropertyValue('--border').trim(), lineColor: colors.getPropertyValue('--blue').trim(),
          clusterBkg: colors.getPropertyValue('--panel').trim(), clusterBorder: colors.getPropertyValue('--border').trim(),
          edgeLabelBackground: colors.getPropertyValue('--background').trim(),
        },
      });
      const { svg } = await mermaid.render(`guided-map-${++renderId}`, source);
      if (requestedKey !== key) return;
      canvas.innerHTML = DOMPurify.sanitize(svg, { USE_PROFILES: { svg: true, svgFilters: true } });
      renderedKey = key;
      ui['map-status'].textContent = `Versione ${diagram.revision}`;
      fit();
    };
    const result = renderQueue.then(draw, draw);
    renderQueue = result.catch(() => {
      if (requestedKey === key) {
        requestedKey = null;
        ui['map-status'].textContent = 'Disegno non riuscito';
      }
    });
  }

  function toggle() {
    panel.hidden = !panel.hidden;
    ui['map-toggle'].setAttribute('aria-expanded', String(!panel.hidden));
    if (panel.hidden) { ui['map-toggle'].focus(); return; }
    const bounds = panel.getBoundingClientRect();
    place(position && Number.isFinite(position.x) && Number.isFinite(position.y) ? position : { x: bounds.x, y: bounds.y });
    render();
  }

  ui['map-toggle'].addEventListener('click', toggle);
  ui['map-close'].addEventListener('click', toggle);
  ui['map-fit'].addEventListener('click', fit);
  ui['map-zoom-in'].addEventListener('click', () => zoom(scale * ZOOM_FACTOR));
  ui['map-zoom-out'].addEventListener('click', () => zoom(scale / ZOOM_FACTOR));
  ui['map-expand'].addEventListener('click', () => {
    const expanded = panel.classList.toggle('map-expanded');
    ui['map-expand'].replaceChildren(createElement(expanded ? Minimize2 : Maximize2));
    ui['map-expand'].title = expanded ? 'Riduci mappa' : 'Espandi mappa';
    ui['map-expand'].setAttribute('aria-label', ui['map-expand'].title);
    ui['map-expand'].setAttribute('aria-expanded', String(expanded));
    fit();
  });
  ui['map-source-toggle'].addEventListener('click', () => {
    const showingSource = ui['map-source'].hidden;
    ui['map-source'].hidden = !showingSource;
    viewport.hidden = showingSource;
    ui['map-source-toggle'].setAttribute('aria-pressed', String(showingSource));
    if (!showingSource) fit();
  });
  ui['map-export'].addEventListener('click', () => {
    const url = URL.createObjectURL(new Blob([diagram.source], { type: 'text/plain;charset=utf-8' }));
    const link = document.createElement('a');
    link.href = url;
    link.download = `${projectName()}-mappa.mmd`;
    link.click();
    setTimeout(() => URL.revokeObjectURL(url), 0);
  });
  let lastSize = '';
  new ResizeObserver(() => {
    const bounds = panel.getBoundingClientRect();
    const size = `${bounds.width}:${bounds.height}`;
    if (size === lastSize) return;
    lastSize = size;
    if (!panel.hidden) fit();
  }).observe(panel);
  new MutationObserver(render).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
  return {
    update(next) {
      if (diagram?.revision === next?.revision) return;
      diagram = next;
      ui['map-source'].value = next?.source || '';
      ui['map-export'].disabled = !next;
      render();
    },
  };
}
