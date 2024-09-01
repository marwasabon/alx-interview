#!/usr/bin/python3

"""Write a script that reads stdin line by line and computes metrics"""

import sys
import re


def print_stats(status_counts, total_size):
    """Prints the collected statistics."""
    print("File size: {:d}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print("{}: {:d}".format(status_code, status_counts[status_code]))

status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

line_count = 0
total_size = 0

try:
    for line in sys.stdin:
        line_count += 1
        
        parts = line.split()
        if len(parts) < 7:
            continue

        try:
            file_size = int(parts[-1])
            total_size += file_size
        except ValueError:
            continue

        status_code = parts[-2]
        if status_code in status_counts:
            status_counts[status_code] += 1

        if line_count % 10 == 0:
            print_stats(status_counts, total_size)

except KeyboardInterrupt:
    print_stats(status_counts, total_size)

# Final print of statistics in case of termination
print_stats(status_counts, total_size)
