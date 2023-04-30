*This script is designed to convert a protein sequence alignment file in FASTA format to A3M format*

Here's a brief overview of the script:

    Import necessary libraries from BioPython and the sys library.
    Define a function fasta_to_a3m() that takes an input FASTA file and an output file name as its arguments.
    Read and parse the input FASTA file using BioPython's SeqIO.parse().
    Initialize an empty list to store A3M-formatted sequences.
    Store the reference sequence (first sequence in the FASTA file).
    Loop through each sequence record in the FASTA file and convert the sequence to A3M format by making the matched residues upper case and non-matched residues lower case.
    Create a new SeqRecord object with the A3M-formatted sequence and add it to the list of A3M-formatted sequences.
    Write the A3M-formatted sequences to the output file using BioPython's SeqIO.write() function.
    The main function is executed when the script is called from the command line, which takes the input and output file names as command line arguments and calls the fasta_to_a3m() function to convert the input FASTA file to A3M format.
