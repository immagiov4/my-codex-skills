import { Download, GripHorizontal, NotebookPen, Save, X, createElement } from 'lucide';
import { makeFloatingPanel } from './floating_panel.js';

export function setupNotebook(ui, api, projectName) {
  for (const [id, icon] of [['notes-toggle', NotebookPen], ['notes-export', Download], ['notes-grip', GripHorizontal], ['notes-close', X], ['notes-save', Save]]) {
    ui[id].append(createElement(icon));
  }
  let notes = { text: '', position: null };
  let loaded = false;
  let loading = null;
  let pending = null;
  let saving = false;
  const place = makeFloatingPanel({ panel: ui.notebook, handle: ui['notes-drag'], onPosition: position => { notes.position = position; }, onRelease: save });

  async function save() {
    if (!loaded) return;
    notes.text = ui['notes-text'].value;
    pending = { text: notes.text, position: notes.position };
    if (saving) return;
    saving = true;
    ui['notes-status'].textContent = 'Salvataggio...';
    ui['notes-save'].hidden = true;
    try {
      while (pending) {
        const snapshot = pending;
        pending = null;
        await api('/api/notes', { method: 'POST', body: JSON.stringify(snapshot) });
      }
      ui['notes-status'].textContent = 'Salvato';
    } catch {
      ui['notes-status'].textContent = 'Salvataggio non riuscito';
      ui['notes-save'].hidden = false;
    } finally {
      saving = false;
    }
  }

  async function toggle() {
    const opening = ui.notebook.hidden;
    ui.notebook.hidden = !opening;
    ui['notes-toggle'].setAttribute('aria-expanded', String(opening));
    if (!opening) {
      ui['notes-toggle'].focus();
      return;
    }
    if (!loaded) {
      ui['notes-status'].textContent = 'Caricamento...';
      try {
        loading ??= api('/api/notes');
        notes = await loading;
        ui['notes-text'].value = notes.text;
        ui['notes-text'].disabled = false;
        ui['notes-export'].disabled = false;
        loaded = true;
        ui['notes-status'].textContent = 'Salvato';
      } catch {
        loading = null;
        ui['notes-status'].textContent = 'Caricamento non riuscito';
        return;
      }
    }
    if (!ui.notebook.hidden) {
      const bounds = ui.notebook.getBoundingClientRect();
      place(notes.position || { x: bounds.x, y: bounds.y });
      ui['notes-text'].focus();
    }
  }

  ui['notes-toggle'].addEventListener('click', toggle);
  ui['notes-close'].addEventListener('click', toggle);
  ui['notes-text'].addEventListener('input', save);
  ui['notes-save'].addEventListener('click', save);
  ui['notes-export'].addEventListener('click', () => {
    const url = URL.createObjectURL(new Blob([ui['notes-text'].value], { type: 'text/plain;charset=utf-8' }));
    const link = document.createElement('a');
    link.href = url;
    link.download = `${projectName()}-note.txt`;
    link.click();
    setTimeout(() => URL.revokeObjectURL(url), 0);
  });
}
