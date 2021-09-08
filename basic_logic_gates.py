"""
    Module with the basic logic gates (AND, NOT) that can be created with simple circuits.
"""

def and_(input_1, input_2):
    """AND logic gate."""

    _check_binary_args(input_1)

    return int(input_1) and int(input_2)

def not_(input_):
    """NOT logic gate."""

    _check_binary_args(input_)

    return int(not input_)

def _check_binary_args(*args):
    """Function to check that all the arguments are a binary element (0, 1, True, False)."""

    invalid_args_list = [i for i in args if i not in [0, 1, True, False]]

    if invalid_args_list:

        raise Exception(f'Invalid argument/s {invalid_args_list}. Should be one of [0, 1, True, False].')
