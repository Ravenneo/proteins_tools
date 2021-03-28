#!/bin/python3
"""Main Programm"""

from duf_extraction.duf_extraction import CSVConvertion

if __name__ == "__main__":
    convert = CSVConvertion("./input")
    convert.convertion()
    print("Done!")
