---
name: code-review
description: "Revisiona un ramo, una PR o modifiche locali con il Codex CLI e GPT-6.1 Sol: ricerche indipendenti, conferma dei rilievi, copertura e consumi misurati. È la procedura di base per la revisione del codice."
---

# Revisione del codice con Sol

Produci un rapporto sul cambiamento fissato, con rilievi sostenuti da percorsi reali,
posizioni controllate, copertura e limiti. Il coordinamento avviene sul computer;
l'inferenza usa l'autenticazione Codex esistente. Il risultato è una revisione
assistita del cambiamento, con il livello di prova indicato per ciascun rilievo.

Usa questa procedura come revisione di base del codice. Fissa sorgenti e contratto,
esegui ricerche indipendenti e verifica ogni candidato prima di confermarlo.

## Fissa il materiale

1. Identifica il contratto dal mandato del maintainer, dalle decisioni approvate e
   dall'issue. Leggi le istruzioni `AGENTS.md` pertinenti. Per un repository remoto,
   confronta la revisione disponibile con `git ls-remote`; annota la revisione
   effettivamente esaminata. Il materiale deve avere un'identità ripetibile. Quando manca una specifica,
   usa il mandato e gli invarianti documentati, registrando i requisiti indeterminati.
2. Prepara una cartella isolata fuori dal repository con `before/`, `after/`,
   `diff.patch`, `contract.md` e `manifest.json`. Per revisioni Git fissate usa
   `git archive` e `git diff --binary --no-ext-diff`. Per una PR, la base del confronto
   è il merge-base effettivo. Per cambiamenti locali acquisisci i file tracciati,
   modificati ed eventuali nuovi file pertinenti, preservando il confronto con HEAD.
   Le cartelle contengono sorgenti e istruzioni; escludi credenziali e dipendenze.
3. Scrivi nel manifest `target`, `changed_files` come percorsi relativi alle due
   versioni, e l'identità delle revisioni quando disponibile. Controlla che ogni
   differenza nei file sia rappresentata dalla patch e dal manifest. Il contratto
   registra anche le decisioni che prevalgono sulle istruzioni del repository.
   Mantieni prove attese e risultati precedenti fuori dal materiale dei revisori.

Il controllo automatico confronta il manifest con i file modificati e congela
l'impronta di tutto il materiale prima delle chiamate. L'esattezza del confronto
Git e l'autorità del contratto sono responsabilità del coordinatore.

## Verifica il CLI e avvia

Leggi `codex --version`, `codex exec --help` e `codex login status`. Usa il CLI
autenticato disponibile. Se serve un aggiornamento, eseguilo con l'autorizzazione
del maintainer. Su Windows individua il vero `codex.exe` dietro il lanciatore npm;
`--codex` riceve quel percorso. Verifica versione e autenticazione senza stampare
credenziali. Usa la documentazione ufficiale quando il CLI cambia comportamento.

Risolvi `$reviewSkill` dalla cartella di questo `SKILL.md`, anche nelle installazioni
come plugin. Esegui `scripts/run_review.py --help`, poi passa la cartella del caso, una cartella
nuova dei risultati esterna al caso, il percorso del CLI e un limite di tempo
per ciascuna chiamata coerente con il mandato tramite `--timeout-seconds`.

```powershell
python "$reviewSkill/scripts/run_review.py" `
  --case $reviewCase --output $reviewOutput --codex $codexExe `
  --timeout-seconds $reviewTimeoutSeconds
```

Se le istruzioni applicabili chiedono un altro modello, registra nel contratto la
decisione autorizzata che risolve il conflitto prima di avviare il CLI.

Lo script seleziona realmente `gpt-6.1-sol` con `-m`, imposta `review_model` nello
stesso processo e usa `model_reasoning_effort=medium`. Verifica modello e livello
nei dati `turn_context` della sessione. Una risposta con modello diverso, contesto
assente o richiesta fallita interrompe la procedura. `--effort xhigh` richiede
`--effort-reason` e una complessità che giustifichi il livello autorizzato.

`--ignore-user-config` mantiene gli override nella singola esecuzione e riusa
l'autenticazione esistente. `--sandbox read-only` e `-a never` regolano gli
strumenti del revisore. Le letture sono circoscritte al caso nelle istruzioni;
la protezione di sola lettura impedisce scritture ma consente letture esterne.
Il coordinatore controlla le trascrizioni per verificare l'ambito effettivo.

## Valuta le prove

Il processo esegue due ricerche in sessioni distinte: contratto e correttezza;
flussi, regressioni e sicurezza. La seconda riceve lo stesso materiale della prima.
Una terza sessione ripercorre ogni candidato e restituisce `accept`, `reject` o
`unverified`, con prova e deduplicazione. Anche con candidati vuoti conserva i
limiti delle letture. Le tre chiamate sono seriali e ogni cartella dei risultati
conserva risposte, eventi, consumo, modello effettivo, durata e impronte.

Controlla ogni candidato con i principi di
[receiving-pr-reviews](../receiving-pr-reviews/SKILL.md): requisito
autorevole, percorso supportato, conseguenza materiale, prova nel cambiamento.
L'accordo tra revisori è un indizio; il codice e le osservazioni sostengono la
decisione. Un dubbio di contratto richiede una decisione del maintainer.
Il mandato di revisione conserva i sorgenti come materiale di sola lettura.

Per confermare un comportamento, esegui una riproduzione leggera in un'altra copia
e confrontala con la base. Coordina i controlli costosi con chi possiede il gate
del repository. Distingui analisi statica, riproduzione eseguita e verifica visiva.
Se una prova resta aperta, conserva il candidato con il suo limite.

## Consegna il risultato

Usa `report.md`, `findings.json` e `metrics.json`. Riporta posizione, gravità,
attivazione, conseguenza, contratto ed evidenza per ogni rilievo confermato;
conserva le decisioni su tutti i candidati, la copertura e le parti da verificare.
Le righe sono riferite alla versione `after`; quando il file è eliminato e assente
in `after`, usa il sorgente e le righe di `before`. Il rapporto indica la versione
accanto alla posizione. Ogni rilievo canonico accettato ha una propria decisione
`accept` riferita a sé stesso; altri candidati accettati possono riferirsi a esso.
Il rapporto conserva `target`, `base` e `head` disponibili nel manifest e riepiloga
il consumo registrato e la somma delle durate delle chiamate seriali.

Controlla negli eventi le letture effettive rispetto alla copertura dichiarata.
Un consumo registrato è una misura della singola esecuzione; un risultato vuoto
descrive soltanto l'ambito e le prove effettivamente raggiunti.

Per la provenienza Qwen e le differenze di copertura leggi
[references/qwen-method.md](references/qwen-method.md). Il processo conserva
ricerca separata e verifica; una prova piccola permette di giudicare quel campione.
