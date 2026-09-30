import './style.css';
import { Compartment, EditorState } from '@codemirror/state';
import { Decoration, EditorView, lineNumbers } from '@codemirror/view';
import { unifiedMergeView } from '@codemirror/merge';
import { oneDark } from '@codemirror/theme-one-dark';
import { defaultHighlightStyle, StreamLanguage, syntaxHighlighting } from '@codemirror/language';
import { javascript } from '@codemirror/lang-javascript';
import { python } from '@codemirror/lang-python';
import { json } from '@codemirror/lang-json';
import { html } from '@codemirror/lang-html';
import { css } from '@codemirror/lang-css';
import { markdown } from '@codemirror/lang-markdown';
import { cpp } from '@codemirror/lang-cpp';
import { lua } from '@codemirror/legacy-modes/mode/lua';
import { ArrowLeft, ArrowRight, Search, createElement } from 'lucide';
import { CodeNavigation } from './code_navigation.js';
import { createMessageRenderer } from './message_markdown.js';
import { setupNotebook } from './notebook.js';
import { setupFileSearch } from './file_search.js';
import { setupPanelLayout } from './panel_layout.js';
import { setupConceptMap } from './concept_map.js';

const token = window.location.hash.slice(1);
const ui = Object.fromEntries([...document.querySelectorAll('[id]')].map(element => [element.id, element]));
const editorTheme = new Compartment();
const codeNavigation = new CodeNavigation();
const renderMessage = createMessageRenderer(window, openFile);
ui['code-back'].append(createElement(ArrowLeft));
ui['code-forward'].append(createElement(ArrowRight));
ui['search-icon'].append(createElement(Search));
let theme = window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
try {
  const savedTheme = localStorage.getItem('guided-theme');
  if (savedTheme === 'light' || savedTheme === 'dark') theme = savedTheme;
} catch { /* The theme also works when browser storage is unavailable. */ }
document.documentElement.dataset.theme = theme;
ui['light-theme'].checked = theme === 'light';
let walkthrough = null;
let viewedStep = null;
let viewedStepId = null;
let followingCurrent = true;
let editor = null;
let shownFile = null;
let lastMessages = '';
let lastHistory = '';
let fileRequest = 0;

function codeTheme() {
  if (theme === 'dark') return oneDark;
  return [
    EditorView.theme({
      '&': { color: '#20252b', backgroundColor: '#ffffff' },
      '.cm-gutters': { color: '#69717c', backgroundColor: '#f3f4f6', borderColor: '#d7dbe1' },
      '.cm-selectionBackground': { backgroundColor: '#d9e8ff' },
    }, { dark: false }),
    syntaxHighlighting(defaultHighlightStyle),
  ];
}

ui['light-theme'].addEventListener('change', () => {
  theme = ui['light-theme'].checked ? 'light' : 'dark';
  document.documentElement.dataset.theme = theme;
  try { localStorage.setItem('guided-theme', theme); }
  catch { /* Keep the selection for this page when storage is unavailable. */ }
  editor?.dispatch({ effects: editorTheme.reconfigure(codeTheme()) });
});

async function api(path, options = {}) {
  const response = await fetch(path, {
    ...options,
    headers: { 'X-Guided-Token': token, ...(options.body ? { 'Content-Type': 'application/json' } : {}) },
    cache: 'no-store',
  });
  if (!response.ok) throw new Error(`Richiesta non riuscita (${response.status})`);
  return response.json();
}

function languageFor(path) {
  const extension = path.split('.').pop()?.toLowerCase();
  if (['js', 'jsx', 'mjs', 'cjs', 'ts', 'tsx'].includes(extension)) {
    return javascript({ typescript: extension === 'ts' || extension === 'tsx', jsx: extension === 'jsx' || extension === 'tsx' });
  }
  if (extension === 'py') return python();
  if (extension === 'json') return json();
  if (['html', 'htm', 'xml'].includes(extension)) return html();
  if (extension === 'css') return css();
  if (['md', 'markdown'].includes(extension)) return markdown();
  if (['c', 'h', 'cc', 'cpp', 'hpp'].includes(extension)) return cpp();
  if (extension === 'lua') return StreamLanguage.define(lua);
  return [];
}

setupNotebook(ui, api, () => walkthrough?.rootName || 'progetto');
setupPanelLayout(ui);
const conceptMap = setupConceptMap(ui, () => walkthrough?.rootName || 'progetto');

function editorPosition() {
  return editor ? { top: editor.scrollDOM.scrollTop, left: editor.scrollDOM.scrollLeft } : null;
}

function showCode(code, { remember = true, position = null } = {}) {
  const { path, content, before = null, startLine = null, endLine = null, kind = null } = code;
  if (remember) codeNavigation.visit(code, editorPosition());
  ui['code-back'].disabled = !codeNavigation.canGoBack;
  ui['code-forward'].disabled = !codeNavigation.canGoForward;
  editor?.destroy();
  ui.editor.replaceChildren();
  const extensions = [
    lineNumbers(), editorTheme.of(codeTheme()), EditorState.readOnly.of(true), EditorView.editable.of(false),
    EditorView.theme({ '&': { height: '100%' }, '.cm-scroller': { overflow: 'auto' } }),
    languageFor(path),
  ];
  if (startLine !== null) {
    extensions.push(EditorView.decorations.of(view => {
      const marks = [];
      for (let line = startLine; line <= endLine && line <= view.state.doc.lines; line++) {
        marks.push(Decoration.line({ class: 'cm-focus' }).range(view.state.doc.line(line).from));
      }
      return Decoration.set(marks);
    }));
  }
  if (before !== null) extensions.push(unifiedMergeView({ original: before, mergeControls: false }));
  editor = new EditorView({ state: EditorState.create({ doc: content, extensions }), parent: ui.editor });
  shownFile = path;
  ui['file-name'].textContent = path;
  ui['code-mode'].textContent = kind === 'change' ? 'Confronto' : kind === 'exploration' ? 'Esplorazione' : 'File';
  ui['code-mode'].className = `mode-badge ${kind || ''}`;
  ui['line-range'].textContent = startLine === null ? '' : startLine === endLine ? `Riga ${startLine}` : `Righe ${startLine}–${endLine}`;
  ui['file-status'].textContent = before !== null ? 'Codice precedente e modifica reale' : '';
  updateSelectedFile();
  const displayedEditor = editor;
  requestAnimationFrame(() => {
    if (editor !== displayedEditor) return;
    if (position) {
      editor.scrollDOM.scrollTop = position.top;
      editor.scrollDOM.scrollLeft = position.left;
    } else if (startLine !== null && startLine <= editor.state.doc.lines) {
      editor.dispatch({ effects: EditorView.scrollIntoView(editor.state.doc.line(startLine).from, { y: 'center' }) });
    }
  });
}

function focusLine(line) {
  if (!viewedStep) return;
  showCode({ path: viewedStep.file, content: viewedStep.after, before: viewedStep.before, kind: viewedStep.kind, startLine: line, endLine: line });
}

function renderAnnotations(step) {
  ui.annotations.replaceChildren();
  for (const annotation of step.annotations) {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'annotation';
    const label = document.createElement('span');
    label.className = 'annotation-line';
    label.textContent = `Riga ${annotation.line}${annotation.side === 'before' ? ' · prima' : ''}`;
    const explanation = document.createElement('span');
    explanation.textContent = annotation.explanation;
    button.append(label, explanation);
    button.addEventListener('click', () => focusLine(annotation.line));
    ui.annotations.append(button);
  }
}

async function showStep(stepId) {
  const step = await api(`/api/step?id=${encodeURIComponent(stepId)}`);
  if (viewedStepId !== stepId) return;
  viewedStep = step;
  ui['step-index'].textContent = `Passo ${step.index}`;
  ui['step-kind'].textContent = step.kind === 'change' ? 'Modifica' : 'Esplorazione';
  ui['step-kind'].className = `kind ${step.kind}`;
  ui['step-title'].textContent = step.title;
  ui['step-overview'].textContent = step.overview;
  ui['step-why'].textContent = step.why;
  ui['why-section'].hidden = false;
  ui['annotations-section'].hidden = false;
  renderAnnotations(step);
  showCode({ path: step.file, content: step.after, before: step.before, startLine: step.startLine, endLine: step.endLine, kind: step.kind });
  renderMessages();
  renderControls();
  renderHistory();
}

function selectStep(stepId) {
  viewedStepId = stepId;
  followingCurrent = stepId === walkthrough.currentStepId;
  showStep(stepId).catch(showDisconnected);
}

function renderHistory() {
  if (!walkthrough) return;
  const key = `${walkthrough.steps.map(step => step.id).join(',')}:${viewedStepId}`;
  if (key === lastHistory) return;
  lastHistory = key;
  ui.history.replaceChildren();
  for (const step of walkthrough.steps) {
    const button = document.createElement('button');
    button.type = 'button';
    button.textContent = `${step.index}. ${step.title}`;
    button.title = step.title;
    if (step.id === viewedStepId) button.className = 'active';
    button.addEventListener('click', () => selectStep(step.id));
    ui.history.append(button);
  }
}

function renderMessages() {
  if (!walkthrough) return;
  const messages = walkthrough.messages.filter(message => message.stepId === viewedStepId);
  const key = `${viewedStepId}:${messages.length}`;
  if (key === lastMessages) return;
  lastMessages = key;
  ui.messages.replaceChildren();
  if (!messages.length) {
    const empty = document.createElement('div');
    empty.className = 'empty-messages';
    empty.textContent = 'Puoi chiedere chiarimenti su questo punto.';
    ui.messages.append(empty);
  }
  for (const message of messages) {
    const bubble = document.createElement('div');
    bubble.className = `message ${message.role}`;
    renderMessage(bubble, message.text);
    ui.messages.append(bubble);
  }
  ui.messages.scrollTop = ui.messages.scrollHeight;
}

function renderControls() {
  if (!walkthrough) return;
  const currentIndex = walkthrough.steps.findIndex(step => step.id === viewedStepId);
  const onCurrent = Boolean(viewedStepId) && viewedStepId === walkthrough.currentStepId;
  ui.previous.disabled = currentIndex < 1;
  ui.next.disabled = currentIndex < 0 || (onCurrent && (walkthrough.released || walkthrough.awaitingAnswer || walkthrough.finished));
  ui.next.textContent = onCurrent ? walkthrough.released ? 'Codex prosegue…' : walkthrough.finished ? 'Completato' : 'Avanti' : 'Passo seguente';
  ui.question.disabled = !onCurrent || walkthrough.awaitingAnswer || walkthrough.finished;
  ui['question-form'].querySelector('button').disabled = ui.question.disabled;
  ui['answer-status'].textContent = walkthrough.awaitingAnswer ? 'Codex risponde…' : '';
  ui['finish-summary'].hidden = !walkthrough.finished;
  ui['finish-summary'].textContent = walkthrough.summary;
}

function showDisconnected() {
  ui.connection.textContent = 'Collegamento interrotto';
  ui.connection.className = 'connection disconnected';
}

async function refresh() {
  if (!token) {
    showDisconnected();
    ui['step-overview'].textContent = 'Apri il collegamento fornito da Codex.';
    return;
  }
  try {
    const nextState = await api('/api/state');
    const previousCurrent = walkthrough?.currentStepId;
    walkthrough = nextState;
    conceptMap.update(nextState.diagram);
    ui.connection.textContent = nextState.finished ? 'Percorso completato' : nextState.awaitingAnswer ? 'Codex risponde…' : nextState.released ? 'Codex prosegue…' : nextState.currentStepId ? 'In attesa di te' : 'Codex al lavoro';
    ui.connection.className = 'connection connected';
    ui['project-name'].textContent = nextState.rootName;
    ui.goal.textContent = nextState.goal;
    if (nextState.currentStepId && (!viewedStepId || (followingCurrent && previousCurrent !== nextState.currentStepId))) {
      viewedStepId = nextState.currentStepId;
      followingCurrent = true;
      await showStep(viewedStepId);
    }
    renderControls();
    renderMessages();
    renderHistory();
  } catch {
    showDisconnected();
  }
}

function updateSelectedFile() {
  document.querySelectorAll('.tree .file').forEach(button => {
    button.classList.toggle('selected', button.dataset.path === shownFile);
  });
}

async function openFile(path, startLine = null, endLine = startLine) {
  const requestId = ++fileRequest;
  try {
    const file = await api(`/api/file?path=${encodeURIComponent(path)}`);
    if (requestId !== fileRequest) return;
    if (startLine !== null && endLine > file.content.split('\n').length) {
      ui['file-status'].textContent = 'Righe fuori dal file';
      return;
    }
    showCode({ path: file.path, content: file.content, startLine, endLine });
  } catch {
    if (requestId === fileRequest) ui['file-status'].textContent = 'File non leggibile';
  }
}

setupFileSearch(ui, api, openFile, updateSelectedFile);
for (const [id, offset] of [['code-back', -1], ['code-forward', 1]]) {
  ui[id].addEventListener('click', () => {
    ++fileRequest;
    const entry = codeNavigation.move(offset, editorPosition());
    if (entry) showCode(entry.code, { remember: false, position: entry.position });
  });
}

async function makeTree(path, host) {
  const { children } = await api(`/api/children?path=${encodeURIComponent(path)}`);
  const list = document.createElement('ul');
  list.className = 'tree-list';
  for (const child of children) {
    const item = document.createElement('li');
    const button = document.createElement('button');
    button.type = 'button';
    button.textContent = child.name;
    button.title = child.path;
    if (child.directory) {
      button.className = 'folder';
      const nested = document.createElement('div');
      let loaded = false;
      button.addEventListener('click', async () => {
        const opening = !button.classList.contains('open');
        button.classList.toggle('open', opening);
        if (opening && !loaded) {
          loaded = true;
          try { await makeTree(child.path, nested); } catch { loaded = false; }
        }
        nested.hidden = !opening;
      });
      item.append(button, nested);
    } else {
      button.className = 'file';
      button.dataset.path = child.path;
      button.addEventListener('click', () => openFile(child.path).catch(showDisconnected));
      item.append(button);
    }
    list.append(item);
  }
  host.replaceChildren(list);
  updateSelectedFile();
}

ui.previous.addEventListener('click', () => {
  const index = walkthrough.steps.findIndex(step => step.id === viewedStepId);
  if (index > 0) selectStep(walkthrough.steps[index - 1].id);
});

ui.next.addEventListener('click', async () => {
  const index = walkthrough.steps.findIndex(step => step.id === viewedStepId);
  if (index < walkthrough.steps.length - 1) {
    selectStep(walkthrough.steps[index + 1].id);
    return;
  }
  ui.next.disabled = true;
  try { await api('/api/event', { method: 'POST', body: JSON.stringify({ type: 'next' }) }); }
  catch { await refresh(); }
  await refresh();
});

ui['question-form'].addEventListener('submit', async event => {
  event.preventDefault();
  const text = ui.question.value.trim();
  if (!text || !viewedStepId || viewedStepId !== walkthrough.currentStepId) return;
  ui.question.disabled = true;
  try {
    await api('/api/event', { method: 'POST', body: JSON.stringify({ type: 'question', text }) });
    ui.question.value = '';
  } catch { /* The current step may have advanced while the question was sent. */ }
  await refresh();
});

refresh();
makeTree('', ui.tree).catch(showDisconnected);
setInterval(refresh, 1500);
