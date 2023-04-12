import os
import re
import sys

def read_fasta_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def find_lpxtg_domains(protein_data):
    pattern = re.compile(r'>(\S+).*?(?:\n|\r\n?)([^>]+)')
    lpxtg_pattern = re.compile(r'LP[A-Z]TG')
    organism_pattern = re.compile(r'\[([^]]+)\]')

    output_file_path = os.path.expanduser('~/Desktop/lpxtg_output.txt')
    with open(output_file_path, 'w') as output_file:
        for wp_number, sequence in pattern.findall(protein_data):
            protein_name = wp_number.split("_")[1]
            organism = organism_pattern.search(wp_number)
            organism = organism.group(1) if organism else "Unknown"

            sequence = sequence.replace('\n', '').replace('\r', '')
            matches = [match.span() for match in lpxtg_pattern.finditer(sequence)]

            if matches:
                output_file.write(f"{wp_number} - {protein_name} - {organism}\n")
                for start, end in matches:
                    output_file.write(f"LPxTG domain at positions {start}-{end}: {sequence[start:end]}\n")
                output_file.write("\n")

if __name__ == "__main__":
    file_path = input("Please enter the path to the .txt file with protein sequences: ")
    file_path = os.path.expanduser(file_path)
    protein_data = read_fasta_file(file_path)
    find_lpxtg_domains(protein_data)
