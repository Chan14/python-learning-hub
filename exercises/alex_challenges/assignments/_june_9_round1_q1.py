# Round 1: List + Dict Drills (Warm-Up)
# Find the second largest number in a list.

# Flatten a 2D list like [[1,2], [3,4], [5]] to [1,2,3,4,5].

# Reverse the keys and values in a dictionary.

# Create a list of random numbers for the assignments.
import random

data = random.sample(range(0, 101), 10)
print(data)


def second_largest(data: list):
    if len(data) <= 1:
        return None
    data.sort()
    return data[-2]


print(f"Second largest is {second_largest(data)}")
# Feedback
# Now let’s dissect it like code surgeons:
# ✅ What You Did Well:
# Seeded randomness for reproducibility — 💯 dev move.
# Edge case check — good thinking with len(data) <= 1.
# Sorting for position-based access — works for most situations.
# Concise logic — readable and direct.
# ⚠️ What Could Go Wrong (and how to improve it):
# Mutating the input list
# You used data.sort(), which modifies the original list in-place.
# If this function is part of a bigger program, it could lead to bugs.
# 🔧 Better: Use sorted(data) to preserve the original.
# Doesn’t handle duplicates
# If data = [4, 4, 4, 4], your function returns the second 4, which isn't the “second largest unique” number.
# So you're getting the second-to-last item, not the second-largest distinct value.
# 🐍 Pythonic Upgrades (to discuss after fixes):
# Convert list to set() first to remove duplicates.
# Use sorted(..., reverse=True) for clarity.
# Consider returning an error message or raising a ValueError for too-few unique values, instead of None.
# Want a challenge?
# 🔥 Try redoing it with all these in mind:
# Do not mutate the original list.
# Ignore duplicates.
# Return None or raise an error if there's no second-largest distinct number.

random.seed(42)
data1 = random.sample(range(0, 20), 5)
data2 = random.sample(range(0, 20), 5)
data = data1 + data2
print(data)


def second_largest_improved_iter1(data: list):
    if not data:
        raise ValueError("Nothing to process")
    uniques = {x for x in data}
    sorted_data = sorted([x for x in uniques])
    if len(sorted_data) < 2:
        return None
    return sorted_data[-2]


# Feedback
# ✅ What You Absolutely Nailed:
# No in-place mutation
# ✔️ You kept the input list untouched. Smart move.
# Removed duplicates using a set
# ✔️ uniques = {x for x in data} — love the clarity here. Pythonic, clean, and no-nonsense.
# Graceful error handling
# ✔️ if not data: followed by a raise—you’ve started thinking defensively. Big step toward robust coding.
# Handles edge cases correctly
# ✔️ Single-value or all-same-value lists return None, as expected.
# Readable and clear
# ✔️ Very easy to follow. No overcomplication. That's a strength.

# ⚙️ Tiny Areas for Polish:
# Set comprehension overkill
# You're doing:
# uniques = {x for x in data}
# That’s fine, but it’s functionally identical to:
# uniques = set(data)
# Unless you’re filtering, the comprehension adds mental noise.
# 🧼 Refactor for simplicity.

# Extra list comp inside sorted()
# You're doing:
# sorted_data = sorted([x for x in uniques])
# But sorted() already takes any iterable. So you can write:
# sorted_data = sorted(uniques)
# 🔍 Cleaner, slightly faster, and idiomatic.


def second_largest_improved_iter2(data: list):
    if not data:
        raise ValueError("Input list is empty")
    uniques = set(data)
    if len(uniques) < 2:
        return None
    return sorted(uniques)[-2]


print(f"Second largest is {second_largest_improved_iter2(data)}")

# 🧠 Stretch Thought (for later):
# What if the list is huge? What if we don’t want to sort the whole thing just to find the second largest?
# That leads to an O(n) one-pass solution with just two variables.

import itertools


def infinite_random_numbers(low=0, high=100):
    """Yields an infinite stream of random integers between `low` and `high`."""
    while True:
        yield random.randint(low, high)


def second_largest_improved_iter3(stream=None, limit=20):
    if limit < 2:
        raise ValueError("sequence has fewer than 2 elements")
    if not stream:
        stream = infinite_random_numbers(0, 100)
    first, second = None, None
    for n in itertools.islice(stream, limit):
        print(n, end=" ")
        if first is None:
            first = n
        elif n > first:
            second = first
            first = n
        elif n < first:
            if second is None or n > second:
                second = n
    if second is None:
        raise ValueError(
            "No second largest element. All elements in the sequence are the same."
        )
    return second


print(f"\nSecond largest is {second_largest_improved_iter3(limit=30)}")

# Feedback:
# Type hinting:
# You can add simple type hints for clarity:
# from typing import Optional, Iterator

# def second_largest_improved_iter3(
#     stream: Optional[Iterator[int]] = None, limit: int = 20
# ) -> Optional[int]:
# Documentation (docstring):
# Add a quick docstring explaining what the function does, inputs, outputs, and edge cases.

import itertools
import random

# Extra Pythonic tweaks (just for fun):
# If you wanted to be fancy, you could initialize first and second as float('-inf') to avoid None checks, but your current approach is clearer for most readers.
from typing import Iterator, Optional


def second_largest_improved_iter4(
    stream: Optional[Iterator[int]] = None, limit: int = 20
) -> Optional[int]:
    """
    Find the second largest distinct number in a stream of integers.

    Parameters:
        stream (Optional[Iterator[int]]): A potentially infinite iterator of integers.
            If None, a random infinite generator is used.
        limit (int): Number of elements to process from the stream (default is 20).
            Must be >= 2.

    Returns:
        Optional[int]: The second largest distinct number seen in the first `limit` elements.
            Returns None if not enough unique values exist.

    Raises:
        ValueError: If limit < 2 or the stream is empty.
    """
    if limit < 2:
        raise ValueError("limit must be at least 2")

    if stream is None:
        stream = infinite_random_numbers()

    # Peek to check if stream has any elements
    stream, peek = itertools.tee(stream)
    try:
        _ = next(peek)
    except StopIteration:
        raise ValueError("The input stream is empty.")

    first = second = None

    for n in itertools.islice(stream, limit):
        print(n, end=" ")
        if first is None:
            first = n
        elif n > first:
            second = first
            first = n
        elif n < first:
            if second is None or n > second:
                second = n

    return second


print(f"\nSecond largest is {second_largest_improved_iter4(limit=20)}")

# Discussion on peeking
# 🔍 Do people peek into an iterator in industrial code?
# Yes — but very carefully.
# Peeking into iterators is absolutely a real technique in production systems, especially in:
# Streaming data pipelines (Kafka consumers, Spark streaming, etc.)
# ETL jobs where lazy evaluation is crucial
# Generators for preprocessing/validation before passing downstream

# But:
# It’s done sparingly, intentionally, and almost always with comments explaining why, because
# consuming from an iterator is a one-way trip.

# 🎯 When is peeking justified?
# ✅ Good reasons:
# You want to validate that something is there (as in your function).
# You want to sample or branch behavior based on an initial item.
# You're writing a protocol interpreter or stream processor that inspects tokens/messages
# before consuming the whole thing.

# ❌ Bad reasons:
# Using peek because you didn't structure the data pipeline properly.
# Overengineering simple logic that doesn’t require it.

# 💡 In our case: Does it help to remove the peek variable after peeking?
# Short answer: No need.
# Longer answer:
# 📌 itertools.tee() creates two independent iterators that share a buffer under the hood.
# Once you've done:
# stream, peek = itertools.tee(stream)
# _ = next(peek)
# You can ignore peek after that — it’s safe. But:
# You don’t need to delete or remove it manually.
# Python’s garbage collector will clean it up if it’s not referenced anymore.
# Holding onto peek has a negligible memory footprint after the peek, because its buffer won’t
# grow if it’s unused.
# 🔥 TL;DR
# Question	Answer
# Do pros peek into iterators?	Yes, when it makes sense and they know what they're doing.
# Is peeking safe in this case?	Yes, you’re only looking ahead once and not disrupting the stream.
# Should we remove peek?	Not needed. It’s harmless after the peek, and Python will clean it up.
# Should we comment it?	Yes! In production code, a short comment like “# Check if stream is
# empty without consuming it” is courteous to the future you.

# Bonus move 💡
# If you really wanted to be fancy and avoid tee, you could write a wrapper that does a
# one-time “peek + yield” combo. But in your case, tee is perfect.

# 🔧 The Custom Peek-Wrapper Approach
# We’ll create a generator that:
# Consumes one element to peek.
# Yields it back first.
# Then continues yielding the rest of the original iterator.


def peek_and_restore(stream: Iterator[int]) -> Iterator[int]:
    """
    Peeks into the first element of a stream to verify it's not empty,
    then yields it back and continues with the rest of the stream.
    """
    try:
        first = next(stream)
    except StopIteration:
        raise ValueError("The input stream is empty.")
    yield first
    yield from stream


def second_largest_improved_iter5(
    stream: Optional[Iterator[int]] = None, limit: int = 20
) -> Optional[int]:
    """
    Find the second largest distinct number in a stream of integers.

    Parameters:
        stream (Optional[Iterator[int]]): An iterator of integers.
            If None, a random infinite generator is used.
        limit (int): Number of elements to process.

    Returns:
        Optional[int]: Second largest distinct number, or None if not enough values.
    """
    if limit < 2:
        raise ValueError("limit must be at least 2")

    if stream is None:
        stream = infinite_random_numbers()

    stream = peek_and_restore(stream)

    first = second = None
    for n in iter(stream):
        print(n, end=" ")
        if limit <= 0:
            break
        limit -= 1

        if first is None:
            first = n
        elif n > first:
            second = first
            first = n
        elif n < first:
            if second is None or n > second:
                second = n

    return second


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\nSecond largest is {second_largest_improved_iter5(iter(input_list))}")
