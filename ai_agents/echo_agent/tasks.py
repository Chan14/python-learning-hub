# echo_agent/tasks.py

from tools.summarizer import summarize_text


def handle_task(task_description: str) -> str:
    if "summarize" in task_description.lower():
        print("Okay! Paste the text you'd like summarized:")
        user_input = input(">>> ")
        return summarize_text(user_input)
    elif "idea" in task_description.lower():
        return "I can generate ideas! (Coming soon...)"
    else:
        return "Sorry, I don't know how to do that yet."
