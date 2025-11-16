from fuzzywuzzy import process
from kb import knowledge
from utils import get_greeting, opening_prompt, normalize_text

def find_entity(query):
    alias_map = {}
    for key, info in knowledge.items():
        alias_map[key] = key
        for a in info.get("aliases", []):
            alias_map[a] = key

    best = process.extractOne(query, list(alias_map.keys()))
    if best and best[1] >= 80:
        return alias_map[best[0]]

    for a, k in alias_map.items():
        if a in query:
            return k
    return None

def detect_intent(text):
    if any(w in text for w in ["where", "location", "located"]):
        return "where"
    if any(w in text for w in ["time", "hour", "open", "close", "timing"]):
        return "when"
    if any(w in text for w in ["head", "hod", "who"]):
        return "who"
    return "summary"

def format_response(entity, intent):
    info = knowledge.get(entity, {})
    if intent == "where":
        return f"{entity.upper()} is located at {info.get('location', 'unknown')}."
    if intent == "when":
        return f"{entity.upper()} timings: {info.get('hours', 'unknown')}."
    if intent == "who":
        return f"The Head of {entity.upper()} is {info.get('head', 'unknown')}."
    return f"{entity.upper()} — Location: {info.get('location','-')}, Timings: {info.get('hours','-')}."

def main():
    print(get_greeting())
    name = input("Guide: May I know your name? ").strip().title()
    print(f"Guide: Nice to meet you, {name or 'friend'}!")
    print(opening_prompt())
    print("Type 'exit' to quit.\n")

    last_entity = None
    while True:
        user_input = input(f"{name or 'You'}: ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("Guide: Goodbye! Have a great day.")
            break

        text = normalize_text(user_input)
        entity = find_entity(text)
        if entity:
            last_entity = entity
            intent = detect_intent(text)
            print("Guide:", format_response(entity, intent))
        elif last_entity and "it" in text:
            print("Guide:", format_response(last_entity, "summary"))
        else:
            print("Guide: Sorry, I don’t have information about that yet.")

if __name__ == "__main__":
    main()
