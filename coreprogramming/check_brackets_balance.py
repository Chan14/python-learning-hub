# Given a string containing only square brackets, [],
# check whether the brackets are balanced or not.
# The brackets are said to be balanced if there is a closing bracket for every opening bracket.
# Therefore, your task is to write the check_balance() function, which returns True if the
# brackets are balanced and False if they are not.
# For the sake of simplicity, you can assume that the string will not contain any other
# characters. Example input "[[[[][]]]]" output True


def check_balance(brackets):
    count = 0
    for char in brackets:
        if char == "[":
            count += 1
        elif char == "]":
            count -= 1
        if count < 0:
            return False
    return count == 0


# print(check_balance("[[][]]]]"))
# print(check_balance("[[[[][]]]]"))
# print(check_balance("]"))
