"""Exercise 5 List Functions."""

__author__ = "730562021"


def only_evens(input_list: list[int]) -> list[int]:
    """Given a list, return only the even numbers in that list."""
    i: int = 0
    even_list: list[int] = []
    if len(input_list) < 1:
        return even_list
    while i < len(input_list):
        if input_list[i] % 2 == 0:
            even_list.append(input_list[i])
        i += 1
    return even_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Given two lists, create a new list that is in order of values from first list and then second list."""
    i: int = 0
    resulting_list: list[int] = []
    while i < len(first_list):
        resulting_list.append(first_list[i])
        i += 1
    i = 0
    while i < len(second_list):
        resulting_list.append(second_list[i])
        i += 1
    return resulting_list

def sub(given_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Return a new list that is between the start index and end index - 1."""
    sub_list: list[int] = []
    i: int = 0
    while start_index <= end_index - 1:
        sub_list.append(given_list[start_index])
        start_index += 1
    return sub_list