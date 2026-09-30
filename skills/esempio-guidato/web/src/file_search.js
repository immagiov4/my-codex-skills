export function rankFileMatches(files, query) {
  return files.filter(file => file.searchName.includes(query)).sort((a, b) => a.name.length - b.name.length || (a.path < b.path ? -1 : a.path > b.path ? 1 : 0));
}

export function visibleFileRange(scrollTop, height, rowHeight, count) {
  return { start: Math.floor(scrollTop / rowHeight), end: Math.min(count, Math.ceil((scrollTop + height) / rowHeight)) };
}

export function setupFileSearch(ui, api, openFile, updateSelectedFile) {
  const host = ui['search-results'];
  const input = ui['file-search'];
  const list = document.createElement('ul');
  list.className = 'tree-list search-list';
  const rowHeight = parseFloat(getComputedStyle(host).getPropertyValue('--search-row-height'));
  let fileIndex = null;
  let files = null;
  let matches = [];
  let queryFrame = null;
  let drawFrame = null;

  function draw() {
    if (!matches.length || host.hidden) return;
    const { start, end } = visibleFileRange(host.scrollTop, host.clientHeight, rowHeight, matches.length);
    const rows = document.createDocumentFragment();
    for (let index = start; index < end; index++) {
      const file = matches[index];
      const item = document.createElement('li');
      item.className = 'search-row';
      item.style.top = `${index * rowHeight}px`;
      const button = document.createElement('button');
      button.className = 'file search-result';
      button.dataset.path = file.path;
      button.title = file.path;
      const name = document.createElement('span');
      name.textContent = file.name;
      const folder = document.createElement('small');
      folder.textContent = file.path;
      button.append(name, folder);
      button.addEventListener('click', () => openFile(file.path));
      item.append(button);
      rows.append(item);
    }
    list.replaceChildren(rows);
    updateSelectedFile();
  }

  function scheduleDraw() {
    if (drawFrame !== null) return;
    drawFrame = requestAnimationFrame(() => { drawFrame = null; draw(); });
  }

  async function search() {
    const query = input.value.trim().toLocaleLowerCase();
    if (!query) return;
    try {
      if (!files) {
        host.textContent = 'Ricerca in corso...';
        fileIndex ??= api('/api/files').then(result => result.files.map(file => ({ ...file, searchName: file.name.toLocaleLowerCase() }))).catch(error => { fileIndex = null; throw error; });
        files = await fileIndex;
      }
      if (query !== input.value.trim().toLocaleLowerCase()) return;
      matches = rankFileMatches(files, query);
      host.scrollTop = 0;
      if (matches.length) {
        list.style.height = `${matches.length * rowHeight}px`;
        host.replaceChildren(list);
        draw();
      } else host.textContent = 'Nessun file trovato';
    } catch {
      if (query === input.value.trim().toLocaleLowerCase()) host.textContent = 'Ricerca non disponibile';
    }
  }

  input.addEventListener('input', () => {
    const searching = Boolean(input.value.trim());
    ui.tree.hidden = searching;
    host.hidden = !searching;
    if (queryFrame !== null) cancelAnimationFrame(queryFrame);
    queryFrame = searching ? requestAnimationFrame(() => { queryFrame = null; search(); }) : null;
  });
  host.addEventListener('scroll', scheduleDraw, { passive: true });
  new ResizeObserver(scheduleDraw).observe(host);
}
