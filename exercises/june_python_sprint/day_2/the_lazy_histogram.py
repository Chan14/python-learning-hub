# 🧠 Challenge 2: The “Lazy Histogram”
# 🧩 Problem Statement:
# You are now working with very large logs of text — millions of words. You want to
# count word frequencies, but:
# You don’t want to store all the words in memory at once.
# You need a generator-based solution: words are streamed in one at a time.
# Punctuation rules and cleaning stay the same.
# You’ll update the word count as each word comes in.

# ✍️ Your Task
# Write a function lazy_word_frequency_counter(text: str) that:
# Uses a generator to yield one cleaned word at a time from the input string.
# Counts word frequencies using a standard dictionary (no defaultdict).
# Returns the final word_count dictionary.

# 🔧 Requirements Recap
# Reuse _clean_text() if needed, or rewrite a lazy cleaner.
# No list of words in memory — stream with a yield.
# Must use for word in generator: logic.

# text = "Streaming, streaming! Data? STREAMING."
# print(lazy_word_frequency_counter(text))
# # {'streaming': 3, 'data': 1}

# Ready?
# 👉 Write the generator and the lazy counter. No help unless you want a hint.
from loop_challenge import clean_text


def stream_words(text: str):
    for word in text.split():
        cleaned = clean_text(word)
        if cleaned:
            yield clean_text(word)


def lazy_word_frequency_counter(text: str):
    word_counter = {}
    for word in stream_words(text):
        word_counter[word] = word_counter.get(word, 0) + 1
    return word_counter


def lazy_word_frequency_counter_2(text: str):
    word_counter = {}
    for word in (clean_text(x) for x in text.split()):
        if word:
            word_counter[word] = word_counter.get(word, 0) + 1
    return word_counter


text = "Streaming, streaming! Data? STREAMING."
print(lazy_word_frequency_counter(text))
print(lazy_word_frequency_counter_2(text))
