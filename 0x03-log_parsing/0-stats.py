#!/usr/bin/python3

"""Python Script that reads stdin line by line and computes metrics"""

import sys


def display_stats(dic, size):
    """Display statistics"""
    print("File size: {:d}".format(size))
    for i in sorted(dic.keys()):
        if dic[i] != 0:
            print("{}: {:d}".format(i, dic[i]))


line_count = 0
total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
try:
    for line in sys.stdin:
        if line_count != 0 and line_count % 10 == 0:
            display_stats(status_codes, total_size)

        stlist = line.split()
        line_count += 1

        try:
            total_size += int(stlist[-1])
        except Exception:
            pass

        try:
            if stlist[-2] in status_codes:
                status_codes[stlist[-2]] += 1
        except Exception:
            pass

    display_stats(status_codes, total_size)

except KeyboardInterrupt:
    display_stats(status_codes, total_size)
    raise
