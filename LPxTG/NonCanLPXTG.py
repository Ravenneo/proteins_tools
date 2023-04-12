import re
import os

def find_lpxtg_domains(protein_data):
    lpxtg_motifs = ["LPxTG", "LPxAG", "LPxQG", "LPxSG"]
    for protein_entry in protein_data.split(">")[1:]:
        protein_lines = protein_entry.strip().split("\n")
        wp_number = protein_lines[0].split()[0][1:]
        protein_name = protein_lines[0][len(wp_number)+2:]
        organism = protein_lines[1][1:]
        sequence = "".join(protein_lines[2:]).replace(" ", "").upper()
        for motif in lpxtg_motifs:
            for i in range(len(sequence) - len(motif) + 1):
                if sequence[i:i+len(motif)] == motif:
                    print(f"{wp_number}\t{protein_name}\t{organism}\t{i+1}\t{motif}")

def main():
    # Get the path to the protein sequence file
    protein_file_path = input("Please enter the path to the .txt file with protein sequences: ")

    # Read the contents of the file into a string
    with open(protein_file_path, 'r') as protein_file:
        protein_data = protein_file.read()

    # Find LPxTG domains in the protein sequences
    find_lpxtg_domains(protein_data)

    # Exporting the console output to a txt file in the Desktop
    desktop_path = os.path.expanduser("~/Desktop")
    output_path = os.path.join(desktop_path, "LPxTG_domains.txt")
    with open(output_path, "w") as output_file:
        output_file.write("LPxTG domains found in the protein sequences:\n\n")
        output_file.write("Non-canonical LPxTG motifs:\n\n")
        for protein_entry in protein_data.split(">")[1:]:
            protein_lines = protein_entry.strip().split("\n")
            wp_number = protein_lines[0].split()[0][1:]
            protein_name = protein_lines[0][len(wp_number)+2:]
            organism = protein_lines[1][1:]
            sequence = "".join(protein_lines[2:]).replace(" ", "").upper()
            for motif in ["LPxAG", "LPxQG", "LPxSG"]:
                lpxtg_pattern = motif.replace("x", ".")
                regex = f"{lpxtg_pattern}"
                matches = re.finditer(regex, sequence)
                for match in matches:
                    start, end = match.span()
                    lpxtg_domain = sequence[start:end]
                    output_file.write(f"{wp_number} - {protein_name} - {organism}\n")
                    output_file.write(f"Non-canonical LPxTG domain at positions {start+1}-{end}: {lpxtg_domain}\n\n")

    print(f"Results exported to {output_path}")

if __name__ == "__main__":
    main()
