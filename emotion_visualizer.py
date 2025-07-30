# emotion_visualizer.py - Glyph-based mood visualizer
import tkinter as tk

def display_emotions(emotion):
    glyphs = {
        "hope": "🪩❤️😂🤲",
        "focus": "🧠🔒",
        "lost": "🧭",
        "love": "💗🕊️"
    }
    root = tk.Tk()
    root.title("Glyph Mood Visualizer")
    label = tk.Label(root, text=glyphs.get(emotion, "❓"), font=("Arial", 80))
    label.pack(padx=50, pady=50)
    root.mainloop()

if __name__ == "__main__":
    display_emotions("hope")
