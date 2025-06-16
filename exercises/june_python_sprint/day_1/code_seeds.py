# Definition of Chanchal
emotion = "confident"
intent = f"strategic learning with focus. Emotion = {emotion}"
energy_level = "high"
status = "Flow mode"


def focus_power(
    hours_of_sleep: int, breakfast_rating: int, social_distraction_level: int
):
    focus = (hours_of_sleep + breakfast_rating) / 2 - social_distraction_level
    return focus


fp = focus_power(6, 8, 3)
print(f"Focus power : {fp}")


def is_present() -> bool:
    return True


def is_motivated() -> bool:
    return True


present = is_present()
motivated = is_motivated()

all_set = present and motivated

from datetime import date

name = "Chanchal"
print(f"{name} : {date.today()} - day 1 of Python Sprint. Looking forward to it.")


def express(feeling: str) -> str:
    return f"Today I feel {feeling.lower()}, but still moving forward."


print(express("Inspired"))


def chanchal_speak(state: str) -> str:
    return f"🌀 Not perfect, but {state.upper()} is still a direction."


chanchal_speak("from step 1 to step 2")
from datetime import datetime

name = "Chanchal"


def chanchal_log(mood: str, energy_level: int, python_vibe: str) -> str:
    if energy_level not in range(11):
        raise ValueError(
            f"energy_level needs to be an integer from 0 to 10, {energy_level} was provided."
        )
    tstamp = datetime.now()
    energy = "LOW" if energy_level < 6 else "HIGH"
    return f"{name} at {tstamp}: My mood is {mood.lower()}, energy level is {energy} and python vibe is {python_vibe.lower()}."


print(chanchal_log("excited, driven and focused", 7, "flow mode"))
