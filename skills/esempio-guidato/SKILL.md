---
name: esempio-guidato
description: Esegui una richiesta di modifica o esplorazione del codice come esempio guidato, mostrando nel browser un passo reale alla volta e attendendo domande o Avanti prima di proseguire.
---

# Esempio guidato

Svolgi il compito richiesto nel progetto reale. La pagina locale mostra i punti utili del lavoro; la conversazione Codex rimane il luogo delle decisioni, delle verifiche e della risposta finale.

## Avvio

1. Individua la cartella del progetto e segui le sue istruzioni. Se riprendi un percorso, usa il percorso della sessione conservato e leggi `state --session <sessione>` per ritrovare il passo corrente e la mappa. Se il servizio locale è terminato, riavvia `serve --session <sessione>` come processo in secondo piano prima di leggere lo stato.
2. Per un nuovo percorso, prepara la pagina come indicato sotto e avviala con `python <cartella-di-questa-skill>/scripts/guided.py start --root <cartella-del-progetto> --goal <richiesta>`. Il comando restituisce il percorso della sessione e apre la pagina web.
3. Conserva il percorso della sessione per i comandi successivi. I file temporanei delle spiegazioni possono stare in quella cartella.
4. Cerca, leggi i chiamanti, scegli la modifica minima e rispetta le autorizzazioni del progetto. Pubblica un passo quando hai raggiunto un punto che insegna qualcosa di concreto. Una ricerca senza risultato utile resta nel lavoro interno.

### Preparazione della pagina

Servono Python 3.10 o successivo e Node.js compatibile con le dipendenze di `web/package-lock.json` (Node.js 26 soddisfa i requisiti). Dalla cartella `<skill>/web` esegui `npm ci` e `npm run build`. La preparazione termina quando esiste `web/dist/index.html`; ripeti la compilazione dopo aver aggiornato i sorgenti della pagina.

## Pubblicazione del passo

Scrivi un file JSON con questi campi e passa il suo percorso a `python <skill>/scripts/guided.py publish --session <sessione> --input <passo.json>`:

```json
{
  "kind": "exploration",
  "title": "Dove nasce il totale",
  "overview": "La funzione somma i prezzi ricevuti.",
  "why": "Questo è il punto comune dei chiamanti interessati.",
  "file": "src/cart.py",
  "startLine": 10,
  "endLine": 12,
  "annotations": [
    { "line": 10, "explanation": "Questa riga riceve la sequenza dei prezzi." }
  ],
  "diagram": "flowchart LR\n  prices[\"Prezzi\"] -->|somma| total[\"Totale\"]"
}
```

Il percorso è relativo alla cartella del progetto. Le righe e il codice provengono dal file effettivo: lo strumento lo legge al momento della pubblicazione. Spiega il blocco nel suo insieme e ogni riga che porta la scoperta. Scegli un blocco e una spiegazione leggibili insieme in una schermata. Puoi raggruppare righe vicine quando svolgono una sola funzione; dividi punti lontani o motivazioni diverse.

Parti da cosa accade concretamente e perché serve. Introduci i termini tecnici e la sintassi necessari a capire quel punto, adattandoti alle conoscenze dichiarate dall'utente. Distingui esplicitamente l'esplorazione del codice già presente dalle modifiche che stai applicando.

Ogni pubblicazione include `diagram`: il sorgente completo della mappa cumulativa. Prima di comporlo, leggi la mappa attuale con `state` o dal risultato di `wait`. Conserva concetti, collegamenti e identificatori già introdotti, aggiungendo ciò che il nuovo passo chiarisce. La mappa è unica per il percorso e rimane la stessa anche quando si consulta un passo precedente. Una correzione motivata può sostituire una relazione errata.

Usa `flowchart` Mermaid senza blocchi Markdown, direttive di configurazione, HTML o callback. Scrivi nomi brevi nella lingua della spiegazione, conserva i simboli reali del codice e indica cosa rappresentano le frecce. Raggruppa inizializzazione, proprietà delle risorse e flusso delle richieste quando aiutano la lettura. Rappresenta solo fatti già verificati e spiegati; distingui con una relazione tratteggiata e un'etichetta le modifiche ancora da realizzare. Il comando verifica la sintassi con Mermaid prima di salvare.

Per una modifica, prima di scrivere nel file acquisisci la sua versione corrente:

```text
python <skill>/scripts/guided.py capture --session <sessione> --file <percorso-relativo>
```

Applica la modifica nel progetto. Poi pubblica un passo con `kind: "change"`, lo `snapshotId` restituito da `capture`, le righe modificate e le spiegazioni. Lo strumento ricava il confronto dalle versioni effettive del file e controlla che le righe cambiate ricadano nel passo. Se una modifica tocca regioni distanti, acquisisci e pubblica ciascuna parte separatamente. Per spiegare una riga eliminata, aggiungi `"side": "before"` alla sua annotazione.

## Attesa e domande

Dopo ogni pubblicazione, chiama `python <skill>/scripts/guided.py wait --session <sessione>` e resta in attesa. Il comando restituisce una domanda o `next`:

Confronta lo `stepId` dell'evento con il `currentStepId` restituito da `state`: rispondi o prosegui soltanto per il passo corrente. Per un evento di un passo precedente, torna in attesa del passo corrente.

- Con una domanda, rispondi usando il codice e il contesto della stessa conversazione. Scrivi la risposta in un file di testo, inviala con `answer --session <sessione> --input <risposta.txt>` e torna in attesa. Se la domanda chiede di aggiornare la mappa o la risposta introduce un rapporto utile al riepilogo, aggiorna il sorgente completo in un file `.mmd` e aggiungi `--diagram <mappa.mmd>` allo stesso comando: risposta e mappa vengono salvate insieme.
- Con `next`, riprendi il compito dal punto raggiunto. Rileggi il file prima di usarlo per il passo seguente, perché può essere cambiato durante la pausa.

L'utente può fare domande anche nella conversazione Codex. Rispondi e conserva l'attesa del passo corrente. Codex principale applica le modifiche; eventuali sottoagenti svolgono solo lettura o verifica del codice.

Quando l'utente chiede una pausa, conserva sessione e passo corrente e attendi la richiesta di ripresa. Usa `finish` soltanto quando il compito è concluso e le verifiche richieste sono terminate.

Le risposte sono visualizzate come Markdown. Usa paragrafi brevi, codice fra apici inversi e blocchi delimitati per gli esempi su più righe. Collega le fonti esterne con normali collegamenti Markdown.

Nelle risposte puoi collegare un file e le sue righe con `[testo](code:src/file.cpp#L20)` oppure `[testo](code:src/file.cpp#L20-L28)`. Usa il percorso relativo al progetto e righe verificate. Il collegamento apre il codice nella pagina, conservando la navigazione precedente. La ricerca a sinistra filtra i nomi dei file; il taccuino conserva le note del progetto sul computer e permette di scaricarle come testo.

Per ricostruire o correggere la mappa senza pubblicare un passo, usa `diagram --session <sessione> --input <mappa.mmd>`. L'icona accanto al taccuino apre una finestra spostabile e ridimensionabile con la mappa corrente e l'esportazione Mermaid.

Esegui prove e controlli nel consueto flusso Codex. Comunica lì un esito negativo e mostra nella pagina il successivo passo di correzione quando cambi il codice. Alla fine invia un breve testo con `finish --session <sessione> --input <riepilogo.txt>` e concludi nella conversazione con il risultato e le verifiche svolte.
