# Automotive Diagnostic Assistant

A bilingual (English/French) web-based assistant for automotive diagnostics. Describe your car problem in natural language and get an instant diagnosis, possible causes, and suggested solutions — completely free, offline, and with no API keys.

## Demo

```
User: I hear a loud grinding noise when I press the brake pedal

Assistant:
Diagnosis: Severe brake pad/rotor wear
Possible Solution: Stop driving ASAP. Check brake pads and rotors —
metal-on-metal grinding means pads are gone. Inspect caliper on the
noisy side.
```

```
Utilisateur: la voiture tire d'un cote quand je freine

Assistant:
Diagnosis: Voiture tire d'un cote
Possible Solution: Verifiez pression pneus (inegale), parallelerisme,
etrier frein bloque, suspension usee. Faites tourner les pneus et
parallelerisme.
```

## How It Works

```
User input (EN/FR)
        │
        ▼
┌──────────────────┐
│  Greeting check  │──► "Hello! / Bonjour!" response
└──────────────────┘
        │ not a greeting
        ▼
┌──────────────────┐     ┌─────────────────────┐
│  spaCy NLP       │────►│  tokenize + lemmatize│
│  (en / fr model) │     │  (normalize words)   │
└──────────────────┘     └─────────────────────┘
        │
        ▼
┌──────────────────────────────────┐
│  Rule-based engine (126 rules)   │
│  keyword matching per system     │
└──────────────────────────────────┘
        │
        ▼
  Diagnosis + Solution  (or fallback help message)
```

1. The input is checked against greetings (English/French).
2. **spaCy** tokenizes and lemmatizes the text using `en_core_web_sm` or `fr_core_news_sm` so variations like *"brakes / brake / braking"* or *"freins / freiner"* match the same rule.
3. The normalized words are matched against **126 diagnosis rules** covering 14 vehicle systems in both languages.
4. The best match returns a diagnosis + suggested solution instantly; if nothing matches, a fallback message explains how to give more detail.

## Covered Systems

| System | Examples |
|--------|----------|
| Brakes | Pad wear, grinding, squeaking, soft pedal, vibration, fluid leak, caliper issues |
| Engine | Overheating, smoke, stalling, misfire, oil pressure, check engine light, belts, knocking, rough idle |
| Battery / Electrical | Dead battery, parasitic drain, charging issues, corroded terminals, warning lights |
| Steering | Vibration, pulling, hard steering, noise, excessive play |
| Transmission | Slipping, hard shifting, noise, fluid leak |
| Tires | Uneven wear, puncture, low pressure, vibration |
| Cooling | Coolant leak, low coolant, heater not working |
| AC / Climate | AC not cold, bad smell |
| Exhaust / Emissions | Smoke, exhaust smell, catalytic converter |
| Suspension | Noise, excessive bouncing, worn shocks/struts |
| Fuel System | Fuel pump, clogged filter, poor economy, injectors |
| Starter / Ignition | Clicking, starter not working, key won't start |
| Smoke / Smell | Smoke under hood, burning smell |
| General | Car pulling, dashboard warning lights, shaking, rust |

## Tech Stack

| Technology | Version | Role |
|------------|---------|------|
| Python | 3.12 | Programming language |
| Streamlit | 1.64.0 | Web UI (chat interface, session history) |
| spaCy | 3.7.5 | NLP pipeline: tokenization + lemmatization |
| en_core_web_sm | 3.7.1 | English language model |
| fr_core_news_sm | 3.7.0 | French language model |
| Custom rule engine | — | `nlp/detect.py` — 126 keyword-matching diagnosis rules |

## About the Mistral LLM (not used in final version)

An experiment with a local LLM was attempted during development:

- **Mistral 7B Instruct v0.2** (`mistral-7b-instruct-v0.2.Q4_0.gguf`, ~3.9 GB) is present in `models/`
- It was run via **GPT4All**
- **It is not used in the final app**: 7B quantized models were too slow and unstable for real-time chat (long delays, memory pressure)
- The final version uses the **rule-based engine + spaCy** instead — instant responses, no GPU/RAM requirements, fully offline
- `models/` is **gitignored** (the 3.9 GB file is not pushed to GitHub)
- The Mistral file is kept locally in case you want to experiment further

> If you later want LLM answers, the integration point is `get_response()` in `app/backend.py`.

## Project Structure

```
├── app/
│   ├── __init__.py
│   └── backend.py          # Response logic, greetings, fallbacks
├── nlp/
│   ├── __init__.py
│   └── detect.py           # 126 diagnosis rules (EN/FR) + spaCy loading
├── models/                 # mistral-7b-instruct-v0.2.Q4_0.gguf (local only, gitignored)
├── main.py                 # Streamlit UI entry point
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

### 1. Create virtual environment and install dependencies

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

`requirements.txt` installs Streamlit, spaCy, and both language models.

### 2. Run the app

```powershell
.\venv\Scripts\activate
streamlit run main.py
```

Or if `streamlit` is not recognized:

```powershell
.\venv\Scripts\activate
python -m streamlit run main.py
```

Open **http://localhost:8501** in your browser.

## Example Interactions

**English:**

| You | Assistant |
|-----|-----------|
| `my battery is dead` | Dead battery — Jump-start or replace battery. Check alternator output (13.5-14.5V while running). Clean terminals and check for parasitic drain. |
| `engine overheating after 30 minutes` | Engine overheating — Check coolant level, thermostat, radiator, and water pump. Never open a hot radiator cap. Check for leaks. |
| `steering vibrates at high speed` | Steering vibration — Usually a wheel balance issue — get wheels balanced. Could also be warped rotors, bent wheel, or worn tie rods. |

**Francais:**

| Vous | Assistant |
|------|-----------|
| `la voiture tremble quand je freine` | Disque de frein voile — Vibration au freinage = disque voile. Rectifiez ou remplacez les disques. |
| `le voyant moteur est allume` | Temoins moteur allume — Lisez les codes OBD2 avec un scanner. Causes courantes : capteur O2, catalyseur, MAF, bouchon essence. |
| `batterie a plat` | Batterie a plat — Demarrez avec cables ou remplacez la batterie. Verifiez alternateur (13.5-14.5V en marche). |

## Features

- **126 diagnosis rules** across 14 vehicle systems
- **Bilingual EN/FR** with dedicated rule sets for each language
- **Instant responses** — no API keys, no internet required
- **Lemmatization** via spaCy so users don't need exact wording
- **Conversation history** — last 5 exchanges kept in session
- **Graceful fallback** — asks for more detail when no rule matches
- **100% free and offline**

## License

MIT

## Author

Built as a PFE (Projet de Fin d'Études) project — Automotive Diagnostic Conversational Assistant.
