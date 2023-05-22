##NOT WORKING##

This script is designed to convert a protein sequence alignment file in FASTA format to A3M format*

This script was written to use with roseTTAFold MSA  https://robetta.bakerlab.org/submit.php

Process:

1) **Go to UniProt**

2) **Blast for your two proteins**
![image](https://user-images.githubusercontent.com/41577767/235379387-4e14c1d1-0062-4e04-b242-9292f9c690bf.png)

3) **Downlad in fasta format both files.**

4) **Combine both files:**

``cat File1.fasta File2.fasta > combined.fasta~``

5) **Align the sequences**
 
 ``clustalo -i combined.fasta -o aligned.fasta --force``
 
6) **Use the python script to change the format**
 
 ``python3 fasta_to_a3m.py aligned.fasta File3.a3m``
 
7) **Filter the file**

``hhfilter -i File3.a3m -o filtered_File3.a3m -id 90 -cov 50 -M first``

8) Upload the filtered file to Robetta as MSA


![image](https://user-images.githubusercontent.com/41577767/235379725-a778ba62-69d1-40ff-b9ea-d861da29984a.png)
