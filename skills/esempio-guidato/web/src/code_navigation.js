export function parseCodeLink(target) {
  try {
    const url = new URL(target);
    if (url.protocol !== 'code:') return null;
    const path = decodeURIComponent(url.pathname).replaceAll('\\', '/');
    if (!path || path.startsWith('/') || path.includes(':') || path.split('/').includes('..') || url.search) return null;
    const range = /^#L([1-9]\d*)(?:-L?([1-9]\d*))?$/.exec(url.hash);
    if (!range) return null;
    const startLine = Number(range[1]);
    const endLine = Number(range[2] || range[1]);
    if (!Number.isSafeInteger(startLine) || !Number.isSafeInteger(endLine) || endLine < startLine) return null;
    return { path, startLine, endLine };
  } catch {
    return null;
  }
}

export class CodeNavigation {
  entries = [];
  index = -1;

  get current() { return this.entries[this.index]; }
  get canGoBack() { return this.index > 0; }
  get canGoForward() { return this.index < this.entries.length - 1; }

  savePosition(position) {
    if (this.current) this.current.position = position;
  }

  visit(code, position) {
    this.savePosition(position);
    this.entries.splice(this.index + 1);
    this.entries.push({ code, position: null });
    this.index = this.entries.length - 1;
    return this.current;
  }

  move(offset, position) {
    const destination = this.index + offset;
    if (destination < 0 || destination >= this.entries.length) return null;
    this.savePosition(position);
    this.index = destination;
    return this.current;
  }
}
