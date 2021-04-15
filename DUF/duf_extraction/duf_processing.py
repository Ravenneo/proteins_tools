#!/bin/python3

from Bio import Entrez
from pathlib import Path
import os
import pandas as pd
import subprocess

class Processing:
    """Test"""
    csv_file = None
    data_frame = None
    afa_directory = None
    fasta_dir = None

    def __init__(self, csv_file, afa_directory, email, fasta_dir = "/tmp"):
        self.csv_file = csv_file
        self.data_frame = pd.read_csv(csv_file)
        self.afa_directory = afa_directory
        Entrez.email = email
        self.fasta_dir = fasta_dir

    def get_proteins(self):
        """Extract proteins from the file"""
        proteins = self.data_frame['Protein'].drop_duplicates()
        return proteins.tolist()

    def __write_fasta(self, output_file):
        input_handle = Entrez.efetch(db="protein", id=self.get_proteins(), rettype="fasta")
        output_handle = open(output_file, "w")
        for line in input_handle:
            output_handle.write(line)
        output_handle.close()

    def muscle_protein(self):
        file_name = os.path.basename(self.csv_file)
        fasta_file = Path(self.fasta_dir) / Path("fasta_" + file_name).with_suffix(".txt")
        self.__write_fasta(fasta_file)
        afa_file = Path(self.afa_directory) / Path(file_name).with_suffix(".afa")
        muscle_command = "muscle -clwstrict -in " + str(fasta_file) + " -out " + str(afa_file)
        subprocess.run(muscle_command, shell=True, check=True)
