from nlp.detect import diagnose_issue
import os
import streamlit as st

GREETINGS_EN = ['hello', 'hi', 'hey', 'good morning', 'good evening', 'good afternoon', 'howdy', 'whats up']
GREETINGS_FR = ['bonjour', 'salut', 'bonsoir', 'coucou', 'hey']

GREETING_RESPONSE_EN = (
    "Hello! I'm your Automotive Diagnostic Assistant.\n\n"
    "Describe your car problem in detail (noises, warning lights, handling issues, etc.) "
    "and I'll help you diagnose it and suggest solutions.\n\n"
    "Example: 'My car makes a grinding noise when I brake' or "
    "'The engine overheats after 20 minutes of driving'."
)

GREETING_RESPONSE_FR = (
    "Bonjour ! Je suis votre assistant en diagnostic automobile.\n\n"
    "Decrivez votre probleme de voiture en detail (bruits, voyants, comportement, etc.) "
    "et je vous aiderai a le diagnostiquer avec des solutions.\n\n"
    "Exemple : 'Ma voiture fait un bruit de grincement quand je freine' ou "
    "'Le moteur surchauffe apres 20 minutes de conduite'."
)

UNKNOWN_EN = (
    "I couldn't find a specific match for your problem. Try describing it with more details:\n"
    "- What part of the car is affected? (engine, brakes, wheels, transmission, electrical, etc.)\n"
    "- What happens? (noise, vibration, smoke, warning light, won't start, etc.)\n"
    "- When does it happen? (at startup, while driving, when braking, turning, etc.)\n\n"
    "Example: 'My car pulls to the left when I brake at low speed'"
)

UNKNOWN_FR = (
    "Je n'ai pas trouve de reponse precise. Decrivez votre probleme avec plus de details :\n"
    "- Quelle partie de la voiture ? (moteur, freins, roues, boite, electronique, etc.)\n"
    "- Que se passe-t-il ? (bruit, vibration, fumee, voyant, ne demarre pas, etc.)\n"
    "- Quand ? (au demarrage, en roulant, au freinage, en tournant, etc.)\n\n"
    "Exemple : 'Ma voiture tire vers la gauche quand je freine a faible vitesse'"
)

def _is_greeting(text):
    return text.strip().lower() in GREETINGS_EN or text.strip().lower() in GREETINGS_FR


def get_response(user_input, lang):
    text = user_input.strip()

    if not text:
        return "Please describe your car problem."

    if _is_greeting(text):
        return GREETING_RESPONSE_EN if lang == 'English' else GREETING_RESPONSE_FR

    diagnosis, solution = diagnose_issue(text, lang)
    if diagnosis != 'Unknown issue':
        return f"Diagnosis: {diagnosis}\nPossible Solution: {solution}"

    return UNKNOWN_EN if lang == 'English' else UNKNOWN_FR
