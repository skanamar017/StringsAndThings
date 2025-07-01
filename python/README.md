# StringsAndThings - Python Version

This is the Python equivalent of the Java StringsAndThings lab exercise.

## Overview

The `StringsAndThings` class contains 5 methods that perform various string manipulation tasks:

1. `count_yz(input_str)` - Count words ending in 'y' or 'z'
2. `remove_string(base, remove)` - Remove all instances of a substring
3. `contains_equal_number_of_is_and_not(input_str)` - Check if "is" and "not" appear equally
4. `g_is_happy(input_str)` - Check if all 'g' characters have adjacent 'g' neighbors
5. `count_triple(input_str)` - Count sequences of 3 identical characters

## Getting Started

1. Implement the methods in `strings_and_things.py`
2. Run the tests with: `python -m pytest test_strings_and_things.py -v`
   or `python test_strings_and_things.py`

## Testing

The test file `test_strings_and_things.py` contains comprehensive test cases for all methods, mirroring the Java JUnit tests.

Each method currently returns `None` and needs to be implemented to pass the tests.