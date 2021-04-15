#!/bin/python
"""Main Programm"""

import argparse

def trimming(input_file, output_file):
    """triming a sequences file to be able to run muscle"""
    file = open(input_file, "r")
    file_content = file.read()
    sequences = file_content.split('\n\n')
    output = open(output_file, "w")
    for single_sequence in sequences:
        last_chars = single_sequence.replace('\n', '')[-22:]
        header_name = single_sequence.split('\n')[0]
        output.write(header_name + '\n')
        output.write(last_chars + '\n')
        output.write('\n')
    output.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sequence trimming application.')
    parser.add_argument('-i','--input', help='Input file name', required=True)
    parser.add_argument('-o','--output', help='Output file name', required=True)
    args = parser.parse_args()

    trimming(args.input, args.output)
