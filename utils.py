import datetime
import random
import re

def get_greeting():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        g = "Good morning"
    elif 12 <= hour < 17:
        g = "Good afternoon"
    elif 17 <= hour < 21:
        g = "Good evening"
    else:
        g = "Good night"
    return f"{g}! I'm your Virtual Campus Guide."

def opening_prompt():
    return random.choice([
        "Where would you like to go today?",
        "Ask me about departments, labs or timings.",
        "What can I help you find on campus?",
    ])

def normalize_text(text):
    text = text.lower().strip()
    return re.sub(r"[^\w\s]", " ", text)
