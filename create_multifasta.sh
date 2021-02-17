#!/bin/bash

VAR=$(echo *.faa | xargs ls)

for i in ${VAR}
	do
		cat ${i}>>database.fa

	done
