# Fonti e adattamento

Fonti consultate il 12 ottobre 2026. I collegamenti puntano alle revisioni studiate, così l'adattamento resta confrontabile anche quando i progetti cambiano.

## e-bash

Fonte: [skill-learning di OleksandrKucherenko/e-bash](https://github.com/OleksandrKucherenko/e-bash/blob/26d905b30c65d57c6707049c8ace9aba2d20fe61/.claude/skills/skill-learning/SKILL.md), con i riferimenti su riconoscimento delle lezioni, validazione e contributi. Licenza MIT; il testo è conservato in `licenses/E-BASH-MIT.txt` alla radice della raccolta.

L'adattamento mantiene la ricerca di lezioni riutilizzabili, il confronto con le istruzioni esistenti, la verifica delle prove e la conservazione della conoscenza valida. Riformula i criteri di validazione in base alla portata della modifica: una correzione riprodotta può essere precisa anche dopo un episodio, mentre una generalizzazione richiede verifiche nelle condizioni dichiarate; la popolarità di uno strumento resta un indizio per la ricerca, anziché una prova della validità di una procedura. Affida inoltre le regole di pubblicazione al repository di destinazione.

## Hermes

Fonti: [revisione dell'esperienza](https://github.com/NousResearch/hermes-agent/blob/f594424e58f18ebc2607decaa72f300e0a26a24b/agent/background_review.py), [curator](https://github.com/NousResearch/hermes-agent/blob/f594424e58f18ebc2607decaa72f300e0a26a24b/agent/curator.py) e [comando `/refine`](https://github.com/NousResearch/hermes-agent/blob/f594424e58f18ebc2607decaa72f300e0a26a24b/website/docs/reference/slash-commands.md). Le istruzioni di questo adattamento sono riscritte per Codex; queste fonti documentano i meccanismi studiati.

In Hermes, `/refine` avvia una revisione su una copia della conversazione, eventualmente orientata da un obiettivo. Il codice dà precedenza alla modifica di una skill pertinente già caricata o esistente e richiede una lettura aggiornata prima della scrittura. La revisione della raccolta considera accorpamenti, provenienza, protezioni e recuperabilità; nel codice studiato l'accorpamento tramite modello è facoltativo e disattivato per impostazione predefinita.

Qui quei metodi diventano procedure eseguibili con i file e gli strumenti di Codex: lettura prima della modifica, ricerca del proprietario, riferimenti tematici, verifica dei richiami e copie recuperabili per gli accorpamenti autorizzati. Le preferenze personali restano circoscritte al loro pubblico e la scrittura segue le autorizzazioni dell'ambiente. L'attivazione della skill avviene tramite la normale selezione di Codex o con `$skill-learning-patterns`; l'esecuzione periodica richiede una richiesta e una configurazione proprie.
