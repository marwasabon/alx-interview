#!/usr/bin/python3
"""Python script for UTF-8 Validation"""


def validUTF8(data):
    """method that determines if a given data set
    represents a valid UTF-8 encoding.
    """
    numbers_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if numbers_bytes == 0:

            while mask_byte & i:
                numbers_bytes += 1
                mask_byte = mask_byte >> 1

            if numbers_bytes == 0:
                continue
# this part
            if numbers_bytes == 1 or numbers_bytes > 4:
                return False

        else:
            if not (i & mask_1 and not (i & mask_2)):
                return False

        numbers_bytes -= 1

    if numbers_bytes == 0:
        return True
    return False
