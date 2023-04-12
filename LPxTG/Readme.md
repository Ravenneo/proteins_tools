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

###New scripts for Non-canonical motifs

**NonCanLPXTG.py**

This script takes a file containing protein sequences in FASTA format and looks for LPxTG motifs in them. It identifies non-canonical LPxTG motifs (LPxAG, LPxQG, and LPxSG) using regular expressions, and outputs their positions and amino acid sequences to a text file named "LPxTG_domains.txt" on the desktop. The script also displays the output in the console and notifies the user once the results have been exported to the file.

**show_motifs.py**

**Description:**
This Python script takes a path to a FASTA file containing protein sequences as input and searches for both canonical and non-canonical LPxTG motifs. It prints the results to the console in an easy-to-read format, indicating the WP number, protein name, organism, motif type, and motif position.

**Features:**

    Ability to find both canonical and non-canonical LPxTG motifs
    Displays the WP number, protein name, organism, motif type, and motif position in an easy-to-read format
    Handles input in the FASTA format

**Usage:**

    Open a terminal window and navigate to the directory containing the "show_motifs.py" script.
    Run the script by typing "python3 show_motifs.py" followed by the path to the FASTA file containing the protein sequences.
    The script will print the results to the console.

**Dependencies:**
This script requires Python 3 and the "re" module.
