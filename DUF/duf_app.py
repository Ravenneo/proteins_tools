#!/bin/python3
"""Main Programm"""

from duf_extraction.csv_convert import CSVConvert
from duf_extraction.duf_processing import Processing
from os import listdir
import argparse
import multiprocessing

def run_muscle(output_folder, email, input_file):
    processing_protein = Processing(input_file, output_folder, email)
    processing_protein.muscle_protein()

def execute_duf_processing(input_folder, output_folder, email):
    convert = CSVConvert(input_folder)
    convert.execute()

    pool = multiprocessing.Pool()
    csv_folder = input_folder + "/csv/"
    for file in listdir(csv_folder):
        csv_file_path = csv_folder + file
        pool.apply_async(run_muscle, args=(output_folder, email, csv_file_path,))
    pool.close()
    pool.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sequence trimming application.')
    parser.add_argument('-i','--input', help='Input folder path', required=True)
    parser.add_argument('-o','--output', help='Output folder path', required=True)
    parser.add_argument('-e','--email', help='email for BIO Entrez', required=True)
    args = parser.parse_args()

    execute_duf_processing(args.input, args.output, args.email)
    print("Done!")
