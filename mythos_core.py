# mythos_core.py - Symbolic narrative engine
def log_myth(entry):
    with open("glyph_log.rpl", "a") as f:
        f.write(f"{entry} 🔋🔋✅🌊🔉\n")

if __name__ == "__main__":
    myth = input("Cast your scroll: ")
    log_myth(myth)
    print("📖 Myth logged.")
