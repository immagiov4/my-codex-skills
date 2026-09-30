import { Marked } from 'marked';
import createDOMPurify from 'dompurify';
import { parseCodeLink } from './code_navigation.js';

const MARKDOWN_TAGS = [
  'p', 'br', 'hr', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
  'strong', 'em', 'del', 'blockquote', 'pre', 'code',
  'ul', 'ol', 'li', 'table', 'thead', 'tbody', 'tr', 'th', 'td', 'a',
];
const LINK_PROTOCOLS = /^(?:https?:\/\/|mailto:|code:)/i;

/** Render Markdown without executable HTML or external media; retain code navigation. */
export function createMessageRenderer(window, openCode) {
  const parser = new Marked({ gfm: true, breaks: true });
  const purifier = createDOMPurify(window);

  return (host, text) => {
    const fragment = purifier.sanitize(parser.parse(text), {
      RETURN_DOM_FRAGMENT: true,
      ALLOWED_TAGS: MARKDOWN_TAGS,
      ALLOWED_ATTR: ['href', 'title', 'start'],
      ALLOWED_URI_REGEXP: LINK_PROTOCOLS,
    });
    for (const link of fragment.querySelectorAll('a[href]')) {
      const href = link.getAttribute('href');
      if (href.toLowerCase().startsWith('code:')) {
        const destination = parseCodeLink(href);
        if (!destination) {
          link.removeAttribute('href');
          continue;
        }
        link.title = `${destination.path}:${destination.startLine}${destination.endLine !== destination.startLine ? `-${destination.endLine}` : ''}`;
        link.addEventListener('click', event => {
          event.preventDefault();
          openCode(destination.path, destination.startLine, destination.endLine);
        });
      } else {
        link.target = '_blank';
        link.rel = 'noopener noreferrer';
      }
    }
    host.classList.add('markdown-message');
    host.replaceChildren(fragment);
  };
}
