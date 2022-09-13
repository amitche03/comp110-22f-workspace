"""Algorithms using lists."""

__author__ = "730562021"

def all(given_list: list[int], searched_number: int) -> bool:
    i: int = 0
    is_same: bool = True
    while i <= len(given_list) - 1 and is_same:
        if given_list[i] != searched_number:
            is_same == False
        i += 1
    return is_same

def max(max_list: list[int]) -> int:
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty list")
        i: int = 0
    while i <= len(max_list):


    


