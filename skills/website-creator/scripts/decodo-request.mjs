// Use the official SDK for targets that the pinned CLI does not expose.
import { readFile, writeFile } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const [cliPath, requestPath, outputPath] = process.argv.slice(2);
const cliDirectory = dirname(cliPath);
const sdkUrl = pathToFileURL(resolve(cliDirectory, '../../../sdk-ts/build/esm/index.js'));
const authUrl = pathToFileURL(resolve(cliDirectory, 'auth/services/detect-credential-type.js'));
const { DecodoClient } = await import(sdkUrl.href);
const { detectCredentialType } = await import(authUrl.href);
const token = process.env.DECODO_AUTH_TOKEN;
if (!token) throw new Error('Decodo credential missing.');
try {
  const auth = detectCredentialType(token) === 'apiKey' ? { apiKey: token } : { token };
  const client = new DecodoClient({ webScrapingApi: auth });
  const request = JSON.parse(await readFile(requestPath, 'utf8'));
  const response = await client.webScrapingApi.scrape(request);
  await writeFile(outputPath, JSON.stringify(response));
  console.log('Response saved; inspect the returned content before using it.');
} catch (error) {
  console.error(JSON.stringify({ error: error.name, status: error.statusCode ?? null,
    message: String(error.message).replaceAll(token, '[redacted]') }));
  process.exitCode = 1;
}
