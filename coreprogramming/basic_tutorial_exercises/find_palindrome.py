#  Challenge 1.1 – Palindrome Detector (Basic)
# Function name: is_palindrome

# Task:
# Write a function that takes a string and returns True if it's a
# palindrome (ignoring case and spaces), else False.
# "" is a palindrome


def is_palindrome(text: str) -> bool:
    """
    Return True if the text is a palindrome, ignoring spaces and case.
    """
    if not text:
        return True
    left_ptr = 0
    right_ptr = len(text) - 1
    text = text.lower()
    while left_ptr < right_ptr:
        if text[left_ptr] == " ":
            left_ptr += 1
            continue
        elif text[right_ptr] == " ":
            right_ptr -= 1
            continue
        elif text[left_ptr] != text[right_ptr]:
            return False
        left_ptr += 1
        right_ptr -= 1
    return True


# A pythonic, less efficient, shortcut --
def is_palindrome_v2(text: str) -> bool:
    """
    Return True if the text is a palindrome, ignoring spaces and case.
    """
    cleaned = "".join(text.split())
    return cleaned == cleaned[::-1]


print(is_palindrome_v2(""))
print(is_palindrome_v2("abcd"))

# Final thoughts from Chatgpt
# You don’t have to prefer this way — your pointer method is strong and more
# algorithmic (and interview-friendly).
# This one-liner is just the Pythonic shortcut. It's great for writing utilities
# or scripts where readability and brevity are king.
