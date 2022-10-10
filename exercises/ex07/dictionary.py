"""Dictionary Functions."""

__author__ = "730562021"

from curses import keyname


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Invert a dicitonary"""
    inverted_dictionary: dict[str, str] = {}
    if len(dictionary) <= 0:
        return inverted_dictionary
    for key in dictionary:
        inverted_dictionary[dictionary[key]] = key
    return inverted_dictionary


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns most common color."""
    maximum_color: str = ""
    maximum_tracker: dict[str, int] = {}
    if len(dictionary) <= 0:
        return maximum_color
    for key in dictionary:
        if dictionary[key] in maximum_tracker:
            maximum_tracker[dictionary[key]] += 1
        else: 
            maximum_tracker[dictionary[key]] = 1
    color_counter: int = 0
    maximum_color: str = ""
    for key in maximum_tracker:
        if maximum_tracker[key] > color_counter:
            maximum_color = key
            color_counter = maximum_tracker[key]
    return maximum_color 


def count(given_list: list[str]) -> dict[str, int]:
    """Counting the amount of times a string appears and return that via a dictionary."""
    result_dictionary: dict[str, int] = {}
    for item in given_list:
        