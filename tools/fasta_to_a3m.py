# Import necessary libraries from BioPython
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import sys

# Define a function to convert FASTA format to A3M format
def fasta_to_a3m(input_file, output_file):
    # Read and parse the input FASTA file
    fasta_records = list(SeqIO.parse(input_file, "fasta"))

    # Check if there are any valid sequences in the input file
    if not fasta_records:
        raise ValueError("No valid sequences found in input file")

    # Initialize an empty list to store A3M-formatted sequences
    a3m_records = []

    # Store the reference sequence (first sequence in the FASTA file)
    ref_seq = str(fasta_records[0].seq)

    # Loop through each sequence record in the FASTA file
    for record in fasta_records:
        # Get the current sequence as a string
        seq = str(record.seq)

        # Convert the sequence to A3M format by making the matched residues upper case and non-matched residues lower case
        a3m_seq = ''.join([c.upper() if ref_seq[i] == c else c.lower() for i, c in enumerate(seq)])

        # Create a new SeqRecord with the A3M-formatted sequence
        a3m_record = SeqRecord(Seq(a3m_seq), id=record.id, description=record.description)

        # Add the A3M-formatted sequence record to the list
        a3m_records.append(a3m_record)

    # Write the A3M-formatted sequences to the output file
    with open(output_file, "w") as f:
        SeqIO.write(a3m_records, f, "fasta")

# The main function to run when the script is called from the command line
if __name__ == "__main__":
    # Get the input and output file names from command line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Call the fasta_to_a3m function to convert the input FASTA file to A3M format
    fasta_to_a3m(input_file, output_file)
