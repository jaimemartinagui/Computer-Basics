"""
    Module with binary subtraction functions.
"""

from basic_logic_gates import not_
from binary_addition import general_adder

def general_subtractor(a, b):
    """
    General binary subtractor.
    Subtracts b from a.
    """

    pass

    # negative_b = convert_to_negative(b)

    # return general_adder(a, negative_b)

def convert_to_correct_format(binary_number, negative=False):
    """Function to convert binary numbers to Two's complement format."""

    formatted_number = '0' + binary_number

    if negative:
        inverted_bits_list = [not_(int(bit)) for bit in formatted_number]
        formatted_number    = ''.join(str(bit) for bit in inverted_bits_list)

    return formatted_number
