# mentalsync.py - National reset protocol (patched)
import sys

def breathwork():
    print("🫁 Inhale... 🫁 Hold... 🫁 Exhale...")

def mood_check():
    try:
        mood = input("How do you feel? ")
    except EOFError:
        mood = "neutral"
    print(f"📡 Mood broadcast: {mood} 🧠")

def journal():
    try:
        entry = input("Journal entry: ")
    except EOFError:
        entry = "[AUTO] No journal entry."
    with open("glyph_log.rpl", "a") as log:
        log.write(f"[MENTALSYNC] {entry}\n")

if __name__ == "__main__":
    breathwork()
    mood_check()
    journal()
    print("🔁 Mental sync complete.")
