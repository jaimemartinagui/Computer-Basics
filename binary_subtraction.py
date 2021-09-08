"""
    Module with binary subtraction functions.
"""

from basic_logic_gates import not_
from binary_addition import general_adder

def convert_to_negative(positive_binary_number):
    """Function to convert a positive binary number to negative with the Two's complement approach."""

    if positive_binary_number[0] == '1':
        positive_binary_number = '0' + positive_binary_number

    inverted_bits_list = [not_(int(bit)) for bit in positive_binary_number]
    inverted_number    = ''.join(str(bit) for bit in inverted_bits_list)

    return general_adder(inverted_number, '1')
