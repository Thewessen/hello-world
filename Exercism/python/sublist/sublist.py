"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 'Sublist'
SUPERLIST = 'Superlist'
EQUAL = 'Equal'
UNEQUAL = 'Unequal'


def is_part(list_a: list, list_b: list) -> bool:
    """Checks if list_a is a sublist of list_b"""
    return any(list_b[i:i+len(list_a)] == list_a
               for i in range(len(list_b)-len(list_a)+1))


def sublist(list_one: list, list_two: list) -> str:
    """Checks equality, non-equality, sublist and superlist
    of the relation of two lists"""
    if list_one == list_two:
        return EQUAL
    if is_part(list_one, list_two):
        return SUBLIST
    if is_part(list_two, list_one):
        return SUPERLIST
    return UNEQUAL
