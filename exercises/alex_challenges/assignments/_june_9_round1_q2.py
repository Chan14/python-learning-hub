# Challenge Flatten a 2D list like [[1,2], [3,4], [5]] to [1,2,3,4,5].
import itertools
from collections.abc import Iterable, Iterator
from typing import Any


def flatten_lists(input_list: list) -> list:
    result = []
    for inner_list in input_list:
        for element in inner_list:
            result.append(element)
    return result


def flatten_lists_improved_with_list_comprehension(input_list: list) -> list:
    return [element for sublist in input_list for element in sublist]


input_list_of_lists = [[1, 2], [3, 4], [5]]
print(flatten_lists_improved_with_list_comprehension(input_list_of_lists))


def flatten_into_an_iterator(input_list: list) -> Iterator[int]:
    return itertools.chain.from_iterable(input_list)


def flatten_list_of_lists(input_list: list) -> list:
    # return [n for n in flatten_into_an_iterator(input_list)]
    return list(flatten_into_an_iterator(input_list))


input_list_of_lists = [[1, 2], [3, 4], [5]]
print(flatten_list_of_lists(input_list_of_lists))


# Feedback -
# Why this is great:
# Your design lets you reuse the lazy iterator anywhere — you could just loop through it,
# feed it into another function, or convert to a list (or another container) only when you want.
# It keeps your code modular, single-responsibility style.
# Memory efficient if you just consume the iterator (e.g., in a for-loop without forcing list

# Tiny tweak suggestion (optional):
# Since flatten_list_of_lists just calls the iterator and wraps it in a list comprehension, it
# could be simplified to:
# def flatten_list_of_lists(input_list: list) -> list:
#     return list(flatten_into_an_iterator(input_list))
# Directly converting the iterator to a list is a bit more idiomatic and marginally faster, but
# your comprehension is perfectly fine! --> implemened above.


# Extended goal - flatten iterators of any level of nesting. Keep strings as is - dont flatten them.


def flatten_recursive(input_data: Iterable):
    """
    Recursively flattens any nested iterable (except str and bytes) into a flat list.

    Args:
        input_data (Iterable): A potentially nested iterable.

    Returns:
        list: A flattened list containing all non-iterable elements.
    """
    return list(_flatten_recursive(iter(input_data)))


def _flatten_recursive(input_data: Iterator):
    for item in input_data:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from _flatten_recursive(iter(item))
        else:
            yield item


data = [1, [2, [3, [4, 5]], [], [[[[6]]]]], 7]
print(flatten_recursive(data))


def flatten_with_stack(input_data: Iterable) -> list:
    result = []
    stack = [iter(input_data)]

    while stack:
        try:
            current = next(stack[-1])
            if isinstance(current, Iterable) and not isinstance(current, (str, bytes)):
                stack.append(iter(current))
            else:
                result.append(current)
        except StopIteration:
            stack.pop()
    return result


data = [1, [2, [3, [4, 5]], [], [[[[6]]]]], 9]
print(flatten_with_stack(data))


def flatten_with_stack_generator(data: Iterable) -> Iterator[Any]:
    stack = [iter(data)]
    while stack:
        try:
            current = next(stack[-1])
            if isinstance(current, Iterable) and not isinstance(current, (str, bytes)):
                stack.append(iter(current))
            else:
                yield current
        except StopIteration:
            stack.pop()


data = [1, [2, [3, [4, 5]], [], [[[[6]]]]], 9]
print(list(flatten_with_stack_generator(data)))
