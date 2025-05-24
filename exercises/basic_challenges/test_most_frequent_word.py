import pytest
from most_frequent_word import most_frequent_word


def test_most_frequent_word_basic():
    text = "Hello hello world"
    chars_to_strip = {"!", "?", ".", ","}
    assert most_frequent_word(text, chars_to_strip) == "hello"


def test_most_frequent_word_with_strip_chars():
    text = "Hello! Hello? HELLO... world, world."
    chars_to_strip = {"!", "?", ".", ","}
    assert most_frequent_word(text, chars_to_strip) == "hello"


def test_most_frequent_word_empty_input():
    text = ""
    chars_to_strip = set()
    assert most_frequent_word(text, chars_to_strip) == ""


def test_most_frequent_word_all_stripped():
    text = "!!! ??? ,,,"
    chars_to_strip = {"!", "?", ".", ","}
    assert most_frequent_word(text, chars_to_strip) == ""


def test_most_frequent_word_tie_lex_smallest():
    text = "apple banana apple banana cherry"
    chars_to_strip = set()
    # Both 'apple' and 'banana' have frequency 2, 'apple' is lexicographically smaller
    assert most_frequent_word(text, chars_to_strip) == "apple"


def test_most_frequent_word_with_digits():
    text = "123 123 456 123"
    chars_to_strip = set()
    assert most_frequent_word(text, chars_to_strip) == "123"


def test_most_frequent_word_strip_spaces_and_letters():
    text = "a a a b b c c c c"
    chars_to_strip = set(["a", " "])
    # 'a' is stripped, so 'c' is most frequent
    assert most_frequent_word(text, chars_to_strip) == "c"
