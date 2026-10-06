---
name: retro
description: "Esamina una sessione di sviluppo e propone miglioramenti agli strumenti, ai controlli e alle istruzioni dell'agente."
---

# Retro

Su richiesta dell'utente, individua miglioramenti all'ambiente di lavoro dell'agente che rendano più affidabili le sessioni successive. Parti dagli errori e dagli attriti osservati nella sessione.

## Procedura

1. Leggi `$writing-for-agents` per valutare le istruzioni destinate agli agenti. Usa `$writing-for-humans` per presentare le conclusioni.
2. Esamina le fonti primarie della sessione indicata: conversazione, registri, comandi, risultati, differenze nei file e decisioni dell'utente. Se manca un riferimento, usa la sessione corrente. Per una sessione precedente, individua i registri disponibili e leggi le parti pertinenti; oscura credenziali e dati personali nelle citazioni. Per un campione di chat, applica prima i filtri richiesti (prodotto, argomento e periodo), poi seleziona il numero richiesto secondo un ordine dichiarato. Verifica la pertinenza nei messaggi, conserva un elenco delle chat e segnala i limiti della copertura. Escludi dal conteggio le chat vuote e i duplicati tecnici della stessa attività; usa le conversazioni collegate come prove dello stesso episodio.
3. Cerca miglioramenti nelle categorie sotto. Per ogni candidato, verifica le istruzioni del progetto, gli strumenti esistenti e chi possiede la regola o il controllo interessato.
4. Presenta i candidati in ordine di conseguenza osservata e utilità. Per ciascuno indica l'episodio con il suo riferimento, la causa sostenuta dalle prove, la modifica proposta, il beneficio atteso e il costo o limite rilevante. Distingui osservazioni e ipotesi. Se le prove sono insufficienti, indica quale verifica permetterebbe di decidere.
5. La richiesta di una retrospettiva autorizza l'analisi e le proposte. Applica le modifiche quando l'utente ne autorizza l'attuazione; rispetta l'ambito di quell'autorizzazione per file, configurazioni, accessi e pubblicazione.

## Categorie

- **Orientamento:** quando trovare un'informazione ha richiesto tentativi ripetuti, valuta un riferimento mirato a un documento o al punto d'ingresso pertinente.
- **Controlli automatici:** leggi prima i comandi di verifica del progetto e la configurazione dell'integrazione continua. Un controllo esistente ma scollegato o guasto può essere la causa. Proponi il controllo più piccolo che intercetti un errore osservato; valuta l'assenza di controlli rispetto al rischio concreto e al loro costo.
- **Regole del codice:** distingui errori meccanici e decisioni che richiedono giudizio. Per i primi, preferisci un controllo deterministico negli strumenti già presenti. Per le seconde, chiarisci la regola nel documento che già la possiede e indica come dovrebbe valutarla la revisione.
- **Istruzioni condivise:** esamina `AGENTS.md`, le istruzioni globali applicabili e l'eventuale `CLAUDE.md`. Valuta riferimenti mirati quando un catalogo lungo occupa il contesto di ogni sessione. Mantieni l'autorità e le preferenze dell'utente.
- **Costo degli strumenti:** cerca chiamate ripetute o risultati troppo estesi rispetto alla domanda; proponi una lettura più mirata o il riuso di uno strumento disponibile.
- **Istruzioni inefficaci:** confronta la regola con il comportamento osservato. Chiarisci il punto che conduce alla decisione errata, mantenendo ogni significato in una sola sede.
- **Accesso alle informazioni:** quando manca una prova necessaria, valuta registri disponibili o accessi in sola lettura. Una proposta di accesso conserva le autorizzazioni richieste dal servizio.

## Documenti e revisione

Usa i documenti esistenti: `AGENTS.md` per i riferimenti operativi, le regole del codice nel documento scelto dal progetto, la documentazione come fonte e le skill per procedure richiamabili. Crea un nuovo documento solo quando la responsabilità lo giustifica.

Chi implementa e chi revisiona segue le regole applicabili. La revisione riceve le fonti necessarie a verificare il cambiamento: requisiti, istruzioni, contesto pertinente e differenze. Una regola nuova deve prevenire il problema osservato senza aggiungere obblighi estranei al mandato.
