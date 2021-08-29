"""
    Module with other logic gates (NAND, OR, XOR) created from the basic ones.
"""

from basic_logic_gates import and_, not_

def nand_(input_1, input_2):
    """NAND logic gate."""

    return not_(and_(input_1, input_2))

def or_(input_1, input_2):
    """OR logic gate."""

    return nand_(not_(input_1), not_(input_2))

def xor_(input_1, input_2):
    """XOR logic gate."""

    return and_(nand_(input_1, input_2), or_(input_1, input_2))
