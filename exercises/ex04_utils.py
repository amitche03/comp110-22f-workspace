"""Algorithms using lists."""

__author__ = "730562021"

def all(given_list: list[int], searched_number: int) -> bool:
    i: int = 0
    is_same: bool = True
    while i <= len(given_list) - 1 and is_same:
        if given_list[i] != searched_number:
            is_same = False
        i += 1
    return is_same

def max(max_list: list[int]) -> int:
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty list")
    i: int = 0
    largest_int: int = max_list[0]
    while i <= len(max_list) - 1:
        if largest_int < max_list[i]:
            largest_int = max_list[i]
        i += 1
    return largest_int

def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    i: int = 0
    is_same: bool = True 
    while i <= len(first_list) - 1 and is_same:
        if first_list[i] != second_list[i]:
            is_same = False
        i += 1
    return is_same



        






    


