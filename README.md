# Tinder 2
 un tinder per piffy

## Assegnazione 
Si vuole realizzare una applicazione di matchmaking di profili. L'esatto tema dell'applicazione è lasciato alla vostra fantasia: potrebbe essere appuntamenti (stile Tinder), oppure accoppiamenti di cani di razza, avversari per partite di tennis, paddle o calcio. Indipendentemente dal tema scelto, il progetto dovrà prevedere i seguenti casi d'uso: 

1. Inserimento e modifica profilo, con tutte le caratteristiche che ritenete utili al contesto. 
2. Ricerca di profili compatibili, indicando una o più categorie, magari indicando una tolleranza (se non sono proprio uguali, almeno simili)
3. Richiesta di contatto e conseguente accettazione/rifiluto.  In caso di accettazione deve essere possibile proporre una data e un'ora per l'incontro.
4. Valutazione del contatto, se accettato, secondo vari parametri. Uno, obbligatorio, è l'affidabilità. 



## Cosa consegnare

1. Un "hello world" del database, in cui mostrate che il sistema è installato, avviato, e si può usare
2. Uno schema della progettazione concettuale del database (UML o ER)
3. Una traduzione dello schema in progettazione logica; questo è particolarmente interessante nel caso dei db NoSQL, che risulterà MOLTO diversa dalla progettazione logica SQL (se così non fosse....meditate)
4. Una presentazione di max 5 slide in cui presentate il vostro "prodotto" e il database utilizzato (tranne nel caso di mysql)
5. L'applicazione, che può essere sia locale, sia web, completa di sorgente
6. Una mini-relazione in cui spiegate (a) il contributo personale di ognuno (b) un vostro commento sul database utilizzato , in particolare quanto lo avete trovato adatto al vostro progetto. 
    
    
## Requisiti
- consegna su gitlab scuola
- uso del DBMS CassandraDB


# Mini-relazione

## La divisione dei compiti
Macchi Alberto:
- backend
- documentazione backend 
- gestione db
- project manager

Schiavone Antonio:
- frontend
- documentazione frontend

## Opinione sul DBMS (CassandraDB)
Per il progetto abbiamo usato una versione cloud di CassandraDB fornita da [DataStax](https://datastax.com) chiamata [Astra](https://astra.datastax.com).
All'inizio è stato complesso capire bene il funzionamento, ci sono stati alti e bassi.
Alcuni problemi riscontrati sono stati:
- Lunghi tempi di connessione;
- Query Language incompleta: manca di funzionalità tipo l'operatore NOT o diverso da per le stringhe nelle condizioni del WHERE.
Ci sono stati anche lati positivi:
- In parte proprietà intrinseca del NoSQL: possibilità di modificare la struttura del DB semplicemente aggiungendo una variabile ad una classe all'interno del file python.
Dopo questa esperienza non farei di questo DBMS la mia prima scelta per i requisiti di questo progetto.


# Documentazione
## Come eseguire i moduli software
## Backend:
- verificare che il proprio computer abbia installato Python (con la sua cartella scripts nel path su Windows)
Ogni volta che viene descritto un comando da eseguire, se `python` non viene trovato come comando provare le alternative `py` o `python3`
- `cd api`
- `pip install -r requirements.txt`
- `cd ..`
- `python -m api`
Sarà ora possibile accedere alle rotte da localhost:5000 (porta modificale in `api/__main__.py`)

## Frontend:
- Verificare che il proprio computer abbia installato NodeJS
- `cd web`
- `npm run dev`
Sarà ora possibile accedere all'interfaccia web da localhost:5600 (porta modificabile dentro a `"dev"` dentro a `"scripts"` in `web/package.json`)