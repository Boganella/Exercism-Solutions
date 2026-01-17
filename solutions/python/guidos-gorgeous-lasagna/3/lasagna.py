"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# Constants
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(bake_time_elapsed):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - bake_time_elapsed


def preparation_time_in_minutes(number_of_layers):
    """Calculate total lasagna preparation time
    :param number_of_layers: int - number of lasagna layers in total
    
    Function multiplies var `number_of_layers` and const`PREPARATION_TIME`
    returns total preparation time per layer
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, bake_time_elapsed):
    """Calculate total cook time

    :param number_of_layers: int - number of lasagna layers in total
    :param bake_time_elapsed: int - number (in minutes) lasagna has spent baking
    
    Function calls func "preparation_time_in_minutes()" passing var `number_of_layers`
    saves return value into var `prep_time`. Then adds `prep_time` to var `bake_time_elapsed`
    finally returns total bake time
    """
    
    prep_time = preparation_time_in_minutes(number_of_layers)
    
    return prep_time + bake_time_elapsed