import { JSDOM } from 'jsdom';

const dom = new JSDOM('');
globalThis.window = dom.window;
globalThis.document = dom.window.document;
const { default: mermaid } = await import('mermaid');
mermaid.initialize({ startOnLoad: false, securityLevel: 'strict' });

let source = '';
for await (const chunk of process.stdin) source += chunk;
try {
  if (!/^flowchart\s+(?:TB|TD|BT|LR|RL)\b/u.test(source.trim()) || /%%\{|^\s*click\s/mu.test(source)) {
    throw new Error('Unsupported diagram configuration');
  }
  await mermaid.parse(source);
  process.stdout.write('valid');
} catch (error) {
  process.stderr.write(String(error.message));
  process.stdout.write('invalid');
  process.exitCode = 1;
} finally {
  dom.window.close();
}
