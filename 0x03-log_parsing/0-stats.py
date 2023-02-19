#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics:"""
import re
import sys


count = 0
file = 0
status_counter = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                  404: 0, 405: 0, 500: 0}


def printCodes(dict, size):
    """Prints the status code and the number of times they it appear"""
    print("File size: {}".format(size))
    for key in sorted(dict.keys()):
        if status_counter[key] != 0:
            print("{}: {}".format(key, dict[key]))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            split_string = re.split('- |"|"| " " ', str(line))
            status_and_size = split_string[-1]
            if count != 0 and count % 10 == 0:
                printCodes(status_counter, file)
            count = count + 1
            try:
                statusC = int(status_and_size.split()[0])
                f_size = int(status_and_size.split()[1])
                if statusC in status_counter:
                    status_counter[statusC] += 1
                file = file + f_size
            except Exception:
                pass
        printCodes(status_counter, file)
    except KeyboardInterrupt:
        printCodes(status_counter, file)
        raise
