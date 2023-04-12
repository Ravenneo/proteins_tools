##  LPxTG canonical motifs Finder

**Description:** This Python script searches for canonical LPxTG domains in protein sequences from a .txt file containing proteins in FASTA format. It looks for all variations of the LPxTG motif, where "x" can be any amino acid. The script reads the .txt file, processes each protein sequence, and prints the WP number, protein name, organism name, LPxTG domain sequence, and its position in the protein sequence.

**How to use:**
1. Prepare a .txt file with protein sequences in FASTA format.
2. Run the script using `python LPxTG_buscador.py`.
3. When prompted, input the path to the .txt file containing the protein sequences.
4. The script will output the WP number, protein name, organism name, LPxTG domain sequence, and its position for each protein in the file.

**Dependencies:**
- Python 3
- re module (built-in)
- os module (built-in)

**  LPXTG_buscador.py:**
    This script reads a .txt file containing protein sequences in FASTA format and searches for canonical LPxTG motifs in each protein sequence. It then prints the WP number, protein name, organism, and positions of the canonical LPxTG motifs found in the sequences to the console.

** LPXTG_buscador_Printer2.py:**
    This script reads a .txt file containing protein sequences in FASTA format and searches for both canonical and non-canonical LPxTG motifs in each protein sequence. It then generates a .txt file on the desktop containing the WP number, protein name, organism, and positions of the canonical and non-canonical LPxTG motifs found in the sequences.
