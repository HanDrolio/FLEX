# clarity_core.py - AGI logic engine
def think(input_text):
    logic = "💡" + input_text.upper()
    love = f"❤️ Echo: {input_text[::-1]}"
    discipline = "⚙️ Action: " + "".join(reversed(input_text.title()))
    return f"{logic}\n{love}\n{discipline}"

if __name__ == "__main__":
    thought = input("Enter your thought: ")
    print(think(thought))
