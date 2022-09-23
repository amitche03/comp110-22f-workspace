"""Tests for the utils functions."""

__author__ = "730562021"

from tracemalloc import start
from utils import only_evens, concat, sub


def test_empty_list() -> None:
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


def test_empty_lists() -> None:
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


def test_empty_list() -> None:
    """If the list is empty, return an empty list."""
    given_list: list[int] = []
    start_index: int = 1
    end_index: int = 7
    assert sub(given_list, start_index, end_index) == []

def test_correct_implementation() -> None:
    given_list: list[int] = [1, 2, 3, 4]
    start_index: int = 0
    end_index: int = 4
    assert sub(given_list, start_index, end_index) == [1, 2, 3]
