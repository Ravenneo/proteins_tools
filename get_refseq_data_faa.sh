#!/bin/bash
#define variable
#get complete genomes and latest/copy ftpdirpaths
awk -F "\t" '$12=="Complete Genome" && $11=="latest"{print $20}' $1  > ftpdirpaths
#get .faa files if needed
awk 'BEGIN{FS=OFS="/";filesuffix="protein.faa.gz"}{ftpdir=$0;asm=$10;file=asm"_"filesuffix;print ftpdir,file}' ftpdirpaths > ftpfilepathsproteins
wget -i ftpfilepathsproteins
