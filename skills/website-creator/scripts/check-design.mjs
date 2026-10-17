import { existsSync } from 'node:fs';
import { homedir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const targets = process.argv.slice(2);
if (!targets.length) {
  process.stderr.write('Usage: node check-design.mjs <markup-file-or-project>\n');
  process.exit(1);
}

const skillRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const candidates = [
  join(skillRoot, '..', 'impeccable', 'scripts', 'detect.mjs'),
  join(process.env.CODEX_HOME || join(homedir(), '.codex'), 'skills', 'impeccable', 'scripts', 'detect.mjs'),
  join(homedir(), '.agents', 'skills', 'impeccable', 'scripts', 'detect.mjs'),
  join(process.cwd(), '.agents', 'skills', 'impeccable', 'scripts', 'detect.mjs'),
];
const detector = candidates.find(existsSync);
if (!detector) {
  process.stderr.write('Installed Node-based Impeccable detector unavailable. Use the installed Impeccable launcher or complete the rendered visual review.\n');
  process.exit(3);
}

const result = spawnSync(process.execPath, [detector, '--json', '--gpt', ...targets], { stdio: 'inherit' });
if (result.error) {
  process.stderr.write(`Impeccable scan failed: ${result.error.message}\n`);
  process.exit(1);
}
process.exit(result.status ?? 1);
