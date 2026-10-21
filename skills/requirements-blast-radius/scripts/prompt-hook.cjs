/** Local prompt-context hook. The model judges scope and message provenance. */
const fs = require('node:fs');
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
if (input.hook_event_name && input.hook_event_name !== 'UserPromptSubmit') process.exit(0);
if (typeof input.prompt !== 'string' || !input.prompt.trim()) process.exit(0);
const instruction = 'Before acting, judge this message against the agreed requirements. For a substantial new request or steering that changes the agreed outcome, run requirements-blast-radius and produce/update its Requirements map. Handle tiny edits and straightforward localized bug fixes directly. For an orchestrator brief already containing a Requirements map section, reuse that map and examine only uncovered changes. The model judges scope and provenance; this hook only injects this instruction.';
process.stdout.write(JSON.stringify({hookSpecificOutput: {hookEventName: 'UserPromptSubmit', additionalContext: instruction}}));
