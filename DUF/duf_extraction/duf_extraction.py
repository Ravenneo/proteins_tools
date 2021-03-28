#!/bin/python3
"""This module extract the afa files from families file."""

from os import listdir
from pathlib import Path
import os
import shutil
import subprocess

class CSVConvertion:
    """Class to convert files from xlsx to csv"""
    input_folder = None

    def __init__(self, input_folder):
        self.input_folder = Path(input_folder)

    def convert_xlsx_to_csv(self, file):
        """Converts a xlsx file to csv"""
        if file.endswith('.xlsx'):
            xlsx_file = self.input_folder / file
            csv_file = Path(file).with_suffix(".csv")
            csv_file_path = self.input_folder / Path(file).with_suffix(".csv")
            subprocess.run("ssconvert " + str(xlsx_file) + " " + str(csv_file_path), \
                shell=True, check=True)
            csv_folder = self.input_folder / "csv"
            if not os.path.isdir(csv_folder) :
                os.mkdir(csv_folder)
            shutil.move(csv_file_path, csv_folder / csv_file)

    def convertion(self):
        """Run convertion process"""
        # Change spaces for underscores in multiples files
        subprocess.run("rename 's/ /_/g' " + str(self.input_folder) + "/*", shell=True, check=True)
        for file in listdir(self.input_folder):
            self.convert_xlsx_to_csv(file)
