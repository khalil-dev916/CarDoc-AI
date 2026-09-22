# Automotive Diagnostic Assistant

A bilingual (English/French) web-based assistant for automotive diagnostics. Describe your car problem in natural language and get instant diagnosis, causes, and solutions.

## Live Demo

```
User: I hear a loud grinding noise when I press the brake pedal

Assistant:
Diagnosis: Severe brake pad/rotor wear
Solution: Stop driving ASAP. Check brake pads and rotors — metal-on-metal
grinding means pads are gone. Inspect caliper on the noisy side.
```

## Features

- **70+ automotive issues** covered in both English and French
- **Instant responses** — no API keys, no internet required
- **Smart keyword matching** — understands natural language descriptions
- **Bilingual** — English and French with dedicated rule sets
- **Web interface** — clean Streamlit UI with conversation history
- **100% free and offline** — runs entirely on your machine

## Covered Systems

| System | Issues Covered |
|--------|---------------|
| Brakes | Pad wear, grinding, squeaking, soft pedal, vibration, fluid leak, caliper issues |
| Engine | Overheating, smoke, stalling, misfire, oil pressure, check engine light, belts, knocking |
| Battery | Dead battery, parasitic drain, charging issues, corroded terminals |
| Steering | Vibration, pulling, hard steering, noise, excessive play |
| Transmission | Slipping, hard shifting, noise, fluid leak |
| Tires | Uneven wear, puncture, pressure, vibration |
| Cooling | Coolant leak, low coolant, heater issues |
| AC | Not cold, bad smell |
| Exhaust | Smoke, smell, catalytic converter |
| Suspension | Noise, bouncing, worn shocks/struts |
| Fuel | Pump, filter, economy, injectors |
| Starter | Clicking, not working, key issues |
| Electrical | Warning lights, burning smell |

## Setup

### 1. Create virtual environment and install dependencies

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Download spaCy language models (optional, for NLP enhancement)

```bash
python -m spacy download en_core_web_sm
python -m spacy download fr_core_news_sm
```

### 3. Run the app

```powershell
.\venv\Scripts\activate
streamlit run main.py
```

Or if `streamlit` is not recognized:

```powershell
.\venv\Scripts\activate
python -m streamlit run main.py
```

Open http://localhost:8501 in your browser.

## Project Structure

```
├── app/
│   ├── __init__.py
│   └── backend.py          # Response logic, greetings, language handling
├── nlp/
│   ├── __init__.py
│   └── detect.py           # 70+ rule-based diagnosis patterns (EN/FR)
├── models/                 # Placeholder for future LLM models
├── main.py                 # Streamlit web UI entry point
├── requirements.txt
└── README.md
```

## How It Works

1. User describes a car problem in English or French
2. System matches keywords against 70+ diagnosis rules
3. Returns the best matching diagnosis with causes and solutions
4. Results are instant with no external API calls

## Example Interactions

**English:**
```
User: my battery is dead
Assistant: Dead battery — Jump-start or replace battery. Check alternator
output (should be 13.5-14.5V while running). Clean terminals and check
for parasitic drain.
```

```
User: engine overheating after 30 minutes of driving
Assistant: Engine overheating — Check coolant level, thermostat, radiator,
and water pump. Never open hot radiator cap. Check for leaks in hoses
and radiator.
```

**Francais:**
```
Utilisateur: ma voiture tremble quand je freine
Assistant: Disque de frein voilé — Vibration au freinage = disque voilé.
Rectifiez ou remplacez les disques. Verifiez le depot inegal de plaquettes.
```

```
Utilisateur: le voyant moteur est allume
Assistant: Temoins moteur allume — Lisez les codes OBD2 avec un scanner.
Causes courantes : capteur O2, catalyseur, MAF, bouchon essence ou rate.
```

## Tech Stack

- **Python 3.12**
- **Streamlit** — web interface
- **spaCy** — NLP processing (optional)
- **Rule-based engine** — 70+ diagnostic patterns

## License

MIT

## Author

Built as a PFE (Projet de Fin d'Etudes) project — Automotive Diagnostic Conversational Assistant.
