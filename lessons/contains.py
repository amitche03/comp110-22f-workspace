"""Example implementing a list utility function."""

#Function name: contains
# we will have 2 parameters: needle (str), haystack (list[str])
# Return type bool
# Gameplan:
# 1. Start with the first index
# 2. Loop Through every index
    #2.A Test if item at index equal to needle
    #2.A. True Return True! We found it!
# 3 Return False


def contains(haystack: list[str], needle: str) -> bool:
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return True
        i += 1
    return False
        