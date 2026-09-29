# Provenienza del processo

La procedura deriva dall'analisi di Qwen Code alla revisione
`b906f937ec041ca9124617bf86726de064bea967`.

- [Documentazione della revisione](https://github.com/QwenLM/qwen-code/blob/b906f937ec041ca9124617bf86726de064bea967/docs/users/features/code-review.md): descrive ambito, livelli e costo delle chiamate.
- [Istruzioni dei ricercatori e verificatori](https://github.com/QwenLM/qwen-code/blob/b906f937ec041ca9124617bf86726de064bea967/packages/cli/src/commands/review/lib/agent-briefs.ts): prescrivono scenari concreti, percorsi fra file, controllo del comportamento rimosso e controprove.
- [Coordinamento effettivo](https://github.com/QwenLM/qwen-code/blob/b906f937ec041ca9124617bf86726de064bea967/packages/core/src/skills/bundled/review/SKILL.md): conserva un elenco cumulativo, verifica le segnalazioni e ricerca le lacune con ricevute delle letture.

L'adattamento locale usa due ricerche indipendenti e una verifica distinta, per
misurare un costo contenuto con Sol. Qwen distribuisce più prospettive e ripete
la ricerca delle lacune fino al criterio di arresto. Questa procedura copre le
prospettive assegnate in una sola raccolta; il rapporto conserva gli aspetti
esaminati e quelli che richiedono altre prove. La copertura dichiarata dai modelli
si controlla contro gli eventi degli strumenti.

Le soglie Qwen riflettono il suo coordinatore. L'estensione di ruoli o tornate qui
richiede un rischio o una lacuna concreta, con costo e scopo concordati.

La documentazione ufficiale Codex descrive
[selezione del modello](https://learn.chatgpt.com/docs/models) ed
[esecuzione non interattiva](https://learn.chatgpt.com/docs/non-interactive-mode).
Il comportamento e le opzioni del CLI installato si verificano con `--help` e con
una richiesta riuscita. Il registro della sessione permette di controllare
modello, ragionamento e protezione effettivi senza leggere credenziali.
