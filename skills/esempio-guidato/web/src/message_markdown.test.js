import assert from 'node:assert/strict';
import test from 'node:test';
import { JSDOM } from 'jsdom';
import { createMessageRenderer } from './message_markdown.js';

test('renders Markdown and preserves file-line navigation', () => {
  const { window } = new JSDOM('<div id="message"></div>');
  const host = window.document.querySelector('#message');
  let opened;
  const render = createMessageRenderer(window, (...location) => { opened = location; });
  render(host, '**Titolo**\n\n- Uno\n- Due\n\n```cpp\nALCdevice *device;\n```\n\n[Codice](code:src/audio.cpp#L20-L28)\n\n[Fonte](https://example.com/source)');
  assert.equal(host.querySelector('strong').textContent, 'Titolo');
  assert.equal(host.querySelectorAll('li').length, 2);
  assert.equal(host.querySelector('pre code').textContent.trim(), 'ALCdevice *device;');
  const codeLink = host.querySelector('a[href^="code:"]');
  const click = new window.MouseEvent('click', { bubbles: true, cancelable: true });
  codeLink.dispatchEvent(click);
  assert.equal(click.defaultPrevented, true);
  assert.deepEqual(opened, ['src/audio.cpp', 20, 28]);
  assert.equal(host.querySelector('a[href^="https:"]').rel, 'noopener noreferrer');
  window.close();
});

test('removes executable HTML, external media and unsafe destinations', () => {
  const { window } = new JSDOM('<div></div>');
  const host = window.document.querySelector('div');
  const render = createMessageRenderer(window, () => assert.fail('Unsafe code link'));
  render(host, '<script>alert(1)</script>\n\n<img src="https://example.com/tracker" onerror="alert(1)">\n\n[Bad](javascript:alert)\n\n[Outside](code:../secret#L1)\n\n<a href="data:text/html,test" onclick="alert(1)">Raw</a>');
  assert.equal(host.querySelector('script, img, [onclick], a[href]'), null);
  assert.match(host.textContent, /Outside/);
  window.close();
});
