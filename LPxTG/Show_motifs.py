import re

def find_lpxtg_domains(protein_data):
    canonical_motif = "LP[A-Z]TG"
    noncanonical_motifs = ["LPxAG", "LPxQG", "LPxSG"]
    canonical_results = []
    noncanonical_results = []

    for protein_entry in protein_data.split(">")[1:]:
        protein_lines = protein_entry.strip().split("\n")
        wp_number = protein_lines[0].split()[0][1:]
        protein_name = protein_lines[0][len(wp_number)+2:]
        organism = protein_lines[0].split("[")[1].split("]")[0]
        sequence = "".join(protein_lines[1:]).replace(" ", "").upper()

        canonical_matches = [(match.start(), match.group()) for match in re.finditer(canonical_motif, sequence)]
        if canonical_matches:
            for match in canonical_matches:
                start, motif = match
                canonical_results.append((wp_number, protein_name, organism, start+1, motif))

        for motif in noncanonical_motifs:
            lpxtg_pattern = motif.replace("x", ".")
            regex = f"{lpxtg_pattern}"
            matches = re.finditer(regex, sequence)
            for match in matches:
                start, end = match.span()
                lpxtg_domain = sequence[start:end]
                noncanonical_results.append((wp_number, protein_name, organism, start+1, lpxtg_domain))

    return canonical_results, noncanonical_results

def main():
    # Get the path to the protein sequence file
    protein_file_path = input("Please enter the path to the .fasta file with protein sequences: ")

    # Read the contents of the file into a string
    with open(protein_file_path, 'r') as protein_file:
        protein_data = protein_file.read()

    # Find LPxTG domains in the protein sequences
    canonical_results, noncanonical_results = find_lpxtg_domains(protein_data)

    # Print canonical results
    print("Canonical LPxTG motifs:")
    for result in canonical_results:
        wp_number, protein_name, organism, start, motif = result
        print(f"{wp_number} - {protein_name} - {organism} - Canonical LPxTG domain at positions {start}-{start+len(motif)-1}: {motif}")

    # Print non-canonical results
    print("Non-canonical LPxTG motifs:")
    for result in noncanonical_results:
        wp_number, protein_name, organism, start, motif = result
        print(f"{wp_number} - {protein_name} - {organism} - Non-canonical LPxTG domain at positions {start}-{start+len(motif)-1}: {motif}")

if __name__ == "__main__":
    main()
