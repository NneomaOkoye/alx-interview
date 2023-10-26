#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): The data set represented by a list of integers.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.

    Notes:
        - A character in UTF-8 can be 1 to 4 bytes long.
        - The data set can contain multiple characters.
        - Each integer represents 1 byte of data, so you only need to handle
          the 8 least significant bits of each integer.
    """

    num_bytes = 0

    for num in data:
        # Check if the current number is a continuation byte
        if num >> 6 == 0b10:
            # If it's not preceded by a valid start byte, return False
            if num_bytes == 0:
                return False
            num_bytes -= 1
        else:
            # Check the number of bytes required for the current character
            if num_bytes != 0:
                return False
            if num >> 7 == 0b0:
                num_bytes = 0
            elif num >> 5 == 0b110:
                num_bytes = 1
            elif num >> 4 == 0b1110:
                num_bytes = 2
            elif num >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False

    # If there are remaining bytes, return False
    return num_bytes == 0
