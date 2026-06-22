# studyassist
Web aplikacija za organizaciju učenja i AI podršku studentima


## Kreiranje zadataka
Ova funkcionalnost omogućava studentu da doda novi zadatak, unese naziv, opis, predmet i rok, kako bi lakše pratio svoje obaveze u aplikaciji StudyAssist.

# StudyAssist AI Agent

StudyAssist AI Agent je jednostavan AI agent razvijen u Python programskom jeziku korišćenjem LangChain framework-a i LLM modela.

Agent je povezan sa temom aplikacije StudyAssist, jer pomaže studentima da na osnovu obaveza, rokova i korisničkog unosa naprave strukturisan plan učenja.

## Funkcionalnosti

- Učitavanje eksternih podataka iz JSON fajla
- Obrada korisničkog unosa kroz terminal
- Korišćenje LLM modela preko LangChain framework-a
- Generisanje strukturisanog Markdown izlaza
- Čuvanje rezultata u fajl `output/plan_ucenja.md`
- Korišćenje `.env` fajla za API ključ

## Struktura projekta

```text
studyassist/
├── main.py
├── requirements.txt
├── README.md
├── .env.example
├── data/
│   └── student_obaveze.json
├── agent/
│   └── study_agent.py
├── services/
│   └── data_loader.py
└── output/
    └── plan_ucenja.md
