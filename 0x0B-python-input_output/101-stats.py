#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys

file_size = 0
status_code = {}
count = 0


def print_stats():
    print("File size: {}".format(file_size))
    for code in sorted(status_code.keys()):
        print("{}: {}".format(code, status_code[code]))


try:
    for line in sys.stdin:
        count += 1

        line = line.strip()
        parts = line.split()

        if len(parts) == 9:
            size = int(parts[-1])
            code = parts[-2]
            file_size += size

            if code in status_code:
                status_code[code] += 1
            else:
                status_code[code] = 1

        if count % 10 == 0:
            print_stats()

    print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
