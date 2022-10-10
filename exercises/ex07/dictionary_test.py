"""Dictionary Testing."""

__author__ = "730562021"

import pytest
from dictionary import invert, favorite_color


# Inverted Tests
def test_empty_dictionary() -> None:
    """Testing for an empty dictionary when given an empty dictionary"""
    dictionary: dict[str, str] = {}
    assert invert(dictionary) == {}


def test_two_strings() -> None:
    """Main use case."""
    dictionary: dict[str, str] = {"Mitchell": "Anderson", "Ben": "Parker"}
    assert invert(dictionary) == {"Anderson": "Mitchell", "Parker": "Ben"}


def test_one_set() -> None:
    """Single set of strings."""
    dictionary: dict[str, str] = {"A": "B"}
    assert invert(dictionary) == {"B": "A"}


# Tests for favorite color function
def test_empty_dictionary() -> None:
    """Returns and empty string if dictionary is empty."""
    dictionary: dict[str, str] = {}
    assert favorite_color(dictionary) == ""


def test_two_matching_colors() -> None:
    """Two matching colors, return the color."""
    dictionary: dict[str, str] = {"Mitchell": "Blue", "Ben": "Blue"}
    assert favorite_color(dictionary) == "Blue"


def test_multiple_colors() -> None:
    """Testing for various colors."""
    dictionary: dict[str, str] = {"Mitchell": "Red", "Ben": "Blue", "Jonah": "Yellow", "Andrey": "Red"}
    assert favorite_color(dictionary) == "Red"


def test_one_color_first() -> None:
    """Singular color comes first."""
    dictionary: dict[str, str] = {"Mitchell": "Purple", "Gabby": "Green"}
    assert favorite_color(dictionary) == "Purple"