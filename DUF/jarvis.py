"""
Jarvis
"""
#!/usr/bin/env python
# coding: utf-8

import csv
import sys
from Bio import Entrez
from Bio import SeqIO

Entrez.email = sys.argv[1]

for record in SeqIO.parse(sys.argv[2], 'fasta'):
    if sys.argv[3] in record.description:
        print(record.id, file=open(sys.argv[3] + 'IDs.txt', 'a'))

list_of_accession = []
with open(sys.argv[3] + 'IDs.txt', 'r', encoding='utf-8-sig') as csvfile:
    efetchin = csv.reader(csvfile, delimiter='\t')
    for row in efetchin:
        list_of_accession.append(str(row[0]))

with open(sys.argv[3] + 'fasta.txt', mode='w') as efetch_output:
    efetch_output = csv.writer(efetch_output, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    input_handle = Entrez.efetch(db="protein", id=list_of_accession, rettype="fasta")
    output_handle = open(sys.argv[3] + 'fasta.txt', "a")
    for line in input_handle:
        output_handle.write(line)

input_handle.close()
output_handle.close()

print('program finished')
