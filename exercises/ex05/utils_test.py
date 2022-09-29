"""Tests for the utils functions."""

__author__ = "730562021"

from utils import only_evens, concat, sub


#evens tests


def test_empty_list_evens() -> None:
    """Testing for an emptty list result when input is an empty list."""
    input_list: list[int] = []
    assert only_evens(input_list) == []


def test_mixed_numbers() -> None:
    """When various numbers are entered, return only the evens."""
    input_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(input_list) == [2.0, 4.0, 6.0]


def test_odd_numbers() -> None:
    """If only odd numbers are entered, return an empty list."""
    input_list: list[int] = [1, 3, 5]
    assert only_evens(input_list) == []


#Concat tests


def test_empty_lists_concat() -> None:
    """If both lists are empty, return an empty list."""
    first_list: list[int] = []
    second_list: list[int] = []
    assert concat(first_list, second_list) == []


def test_two_full_lists() -> None:
    """Concatenate two lists of varying length."""
    first_list: list[int] = [0, 1, 3]
    second_list: list[int] = [9, 7, 9, 10]
    assert concat(first_list, second_list) == [0, 1, 3, 9, 7, 9, 10]


def test_first_empty_second_full() -> None:
    """If one list is empty and another has values, return a list with those values."""
    first_list: list[int] = []
    second_list: list[int] = [9, 7, 9]
    assert concat(first_list, second_list) == [9, 7, 9]


# Sub Tests


def test_empty_list_sub() -> None:
    """If the list is empty, return an empty list."""
    given_list: list[int] = []
    start_index: int = 1
    end_index: int = 7
    assert sub(given_list, start_index, end_index) == []


def test_correct_implementation() -> None:
    """Correct implementation of a lsit with start and end indices."""
    given_list: list[int] = [1, 2, 3, 4]
    start_index: int = 0
    end_index: int = 3
    assert sub(given_list, start_index, end_index) == [1, 2, 3]


def test_negative_number() -> None:
    """Starting from beginning if end index is a negative number."""
    given_list: list[int] = [0, -1, 4, 5]
    start_index: int = -1
    end_index: int = 3
    assert sub(given_list, start_index, end_index) == [0, -1, 4]


def test_start_index_equal_to_len() -> None:
    """If starting index is greater than length of list, return an empty list."""
    given_list: list[int] = [0, 1, 2]
    start_index: int = 3
    end_index: int = 7
    assert sub(given_list, start_index, end_index) == []


def test_end_index_greaster_than_len() -> None:
    """If end index is greater than the length of list, end with last index of list."""
    given_list: list[int] = [1, 2, 3]
    start_index: int = 0
    end_index: int = 4
    assert sub(given_list, start_index, end_index) == [1, 2, 3]


def test_start_index_negative() -> None:
    """If the start index is negative, start from the beginning of list."""
    given_list: list[int] = [0, 1, 3, 4]
    start_index: int = -1
    end_index: int = 3
    assert sub(given_list, start_index, end_index) == [0, 1, 3]