"""
Exercise: Most Frequent Word Finder (Customizable Text Cleaning)

Description:
------------
Given an input text string, this program identifies the word that appears
most frequently after normalizing the text. The normalization process includes:

- Removing user-specified characters (punctuation, whitespaces, or specific letters)
- Converting all alphabetical characters to lowercase
- Retaining only alphanumeric characters not specified for removal

In case of a frequency tie, the lexicographically smallest word is returned.

Usage Example:
--------------
>>> text = "Hello! hello? HELLO... world, world."
>>> chars_to_strip = {"!", "?", ".", ","}
>>> most_frequent_word(text, chars_to_strip)
'hello'
"""


def clean_text(text: str, chars_to_strip: set) -> str:
    """
    Removes specified characters from the input text, converts all letters to lowercase,
    and retains only alphanumeric characters.

    Args:
        text (str): The input word or text fragment to clean.
        chars_to_strip (set): A set of characters to remove from the text.

    Returns:
        str: The cleaned, lowercase version of the word with unwanted characters stripped.
    """
    output_word = []
    for letter in text:
        if letter in chars_to_strip or letter.isspace():
            continue
        elif letter.isalpha():
            output_word.append(letter.lower())
        elif letter.isdigit():
            output_word.append(letter)
    return "".join(output_word)


def most_frequent_word(text: str, chars_to_strip: set) -> str:
    """
    Determines the most frequent word in the given text after cleaning.
    Cleaning includes stripping unwanted characters and normalizing case.

    Args:
        text (str): The input string containing multiple words.
        chars_to_strip (set): Characters to strip from each word before counting.

    Returns:
        str: The most frequent word (lexicographically smallest if there's a tie).
             Returns an empty string if no valid words are found.
    """
    if not text:
        return ""

    word_frequency_table = {}
    max_frequency = 0
    max_frequency_words = []

    words = text.split()

    for word in words:
        cleaned_word = clean_text(word, chars_to_strip)
        if not cleaned_word:
            continue
        count = word_frequency_table.get(cleaned_word, 0) + 1
        word_frequency_table[cleaned_word] = count

        if count > max_frequency:
            max_frequency = count
            max_frequency_words = [cleaned_word]
        elif count == max_frequency:
            max_frequency_words.append(cleaned_word)

    if not max_frequency_words:
        return ""

    return sorted(max_frequency_words)[0]


# === Unit Tests ===
import unittest


class TestMostFrequentWord(unittest.TestCase):
    def test_basic(self):
        text = "Hello! hello? HELLO... world, world."
        chars_to_strip = {"!", "?", ".", ","}
        self.assertEqual(most_frequent_word(text, chars_to_strip), "hello")

    def test_empty_string(self):
        self.assertEqual(most_frequent_word("", {"!", "?", ".", ","}), "")

    def test_all_stripped(self):
        text = "!!! ??? ... ,,,"
        chars_to_strip = {"!", "?", ".", ","}
        self.assertEqual(most_frequent_word(text, chars_to_strip), "")

    def test_tie_break_lex(self):
        text = "apple apple banana banana"
        chars_to_strip = set()
        # Both appear twice; lex smallest 'apple' wins
        self.assertEqual(most_frequent_word(text, chars_to_strip), "apple")

    def test_digits_retained(self):
        text = "abc123 abc123 abc456"
        chars_to_strip = set()
        self.assertEqual(most_frequent_word(text, chars_to_strip), "abc123")


if __name__ == "__main__":
    unittest.main()
