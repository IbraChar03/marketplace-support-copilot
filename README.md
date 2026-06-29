# Marketplace Support Copilot

Un assistente AI per gli operatori di supporto di un marketplace. La demo usa
un marketplace automotive con concessionari e annunci sintetici, ma i pattern
sono applicabili anche a e-commerce, immobiliare e SaaS.

Il progetto non e' un chatbot generico: combina documentazione aziendale,
dati operativi e azioni controllate per aiutare un operatore umano a risolvere
ticket in modo piu' rapido, verificabile e sicuro.

## Problema

Gli operatori del supporto devono consultare policy, controllare dati in sistemi
diversi e preparare risposte coerenti. Questo richiede tempo e rende facile dare
informazioni incomplete o non aggiornate.

Il Copilot riceve il messaggio del dealer, recupera le policy pertinenti,
interroga i dati del marketplace e propone una risposta con fonti. Se serve
modificare lo stato del sistema, propone l'azione e attende l'approvazione umana.

## Utente principale

L'utente principale e' un operatore del supporto interno del marketplace. Il
dealer invia il ticket, ma e' l'operatore a usare il Copilot, verificare la
risposta suggerita e autorizzare eventuali azioni con side effect.

## Flusso principale

1. Arriva un ticket da un dealer.
2. Il sistema identifica se servono documentazione, dati operativi o entrambi.
3. Il RAG recupera le policy pertinenti dalla knowledge base.
4. I tool read-only controllano dealer, annunci e documenti.
5. Il Copilot prepara una risposta con citation e dati verificati.
6. Le azioni write restano pending finche' un operatore non le approva.
7. Trace, tool call, costo, latenza ed esito vengono registrati.

## Esempio

Ticket:

> L'annuncio CAR-123 e' bloccato da due giorni. Perche'?

Il Copilot controlla l'annuncio, trova che manca la foto VIN, recupera la
relativa policy e propone:

> L'annuncio CAR-123 e' bloccato perche' manca una foto leggibile del VIN.
> Dopo il caricamento verra' riesaminato entro 24 ore.
> Fonte: Listing Publication Policy, sezione 3.2.

Se il dealer chiede una revisione manuale, il Copilot prepara l'azione ma non la
esegue finche' l'operatore non la approva.

## MVP

- knowledge base con policy e procedure automotive sintetiche;
- RAG classico con risposta grounded e citation;
- tool read-only per stato annuncio, campi mancanti e onboarding dealer;
- un tool write per richiedere revisione manuale, protetto da approval e
  idempotency;
- API FastAPI con sessione, tracing, costo e gestione errori;
- eval set ripetibile per retrieval, risposta e selezione dei tool;
- interfaccia minima per leggere ticket, risposta suggerita, fonti e azioni.

## Dati

Il progetto usa esclusivamente dati sintetici:

- 5-10 documenti Markdown con policy e procedure;
- 20-30 annunci automotive;
- 5-10 dealer con diversi stati di onboarding;
- ticket di supporto e casi adversariali;
- golden dataset di almeno 30 richieste per gli eval.

Non vengono usati dati, documenti o credenziali reali di aziende.

## Non obiettivi dell'MVP

- nessun agente completamente autonomo;
- nessun multi-agent;
- nessuna computer vision sulle fotografie;
- nessuna stima automatica del prezzo dei veicoli;
- nessuna integrazione con sistemi aziendali reali;
- nessun Kubernetes o infrastruttura distribuita prematura.

## Architettura prevista

```text
UI minima
   |
FastAPI
   |
workflow LangGraph
   |-------------------|
RAG / pgvector      tool operativi / Postgres
   |-------------------|
approval + audit + observability
```

## Strategia di sviluppo

Costruiamo prima un RAG classico misurabile. LangGraph e i tool vengono aggiunti
solo dopo aver verificato retrieval e risposte su un eval set. Ogni incremento
deve avere test o un check oggettivo prima di passare al successivo.

## Stato

Progettazione iniziale. Nessuna funzionalita' e' ancora implementata.
