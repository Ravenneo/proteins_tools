#LPXTG Motive finder
import re
import os


def read_fasta_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content.split(">")[1:]


def find_lpxtg_domains(protein_data):
    protein_info = protein_data.split("\n", 1)[0].strip()
    wp_number = re.search("WP_\d+\.\d+", protein_info).group(0)
    protein_name = re.search("(.+?)\s+\[", protein_info).group(1)
    organism = re.search("\[(.*?)\]", protein_info).group(1)
    
    sequence = "".join(protein_data.split("\n")[1:])
    lpxtg_positions = [m.start() for m in re.finditer(r'LP[A-Z]TG', sequence)]
    
    print(f"{wp_number} - {protein_name} - {organism}")
    if not lpxtg_positions:
        print("No LPxTG domains found.")
    else:
        for pos in lpxtg_positions:
            print(f"LPxTG domain at positions {pos+1}-{pos+5}: {sequence[pos:pos+5]}")
    print("\n")


if __name__ == '__main__':
    file_path = input("Please enter the path to the .txt file with protein sequences: ")
    protein_list = read_fasta_file(os.path.expanduser(file_path))
    
    for protein_data in protein_list:
        find_lpxtg_domains(protein_data)

