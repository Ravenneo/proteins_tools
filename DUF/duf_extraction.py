#!/bin/python3
"""This module extract the afa files from families file."""

from os import listdir
from pathlib import Path
import subprocess

def main():
    """Run process"""
    # Change spaces for underscores in multiples files
    subprocess.run("rename 's/ /_/g' ./input/*", shell=True, check=True)
    for file in listdir("./input/"):
        if file.endswith('.xlsx'):
            print(file)
            xlsx_file = "./input/" + file
            csv_file = "./input/" + Path(file).stem + ".csv"
            subprocess.run("ssconvert " + xlsx_file + " " + csv_file, shell=True, check=True)

if __name__ == "__main__":
    main()
