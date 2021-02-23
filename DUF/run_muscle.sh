#!/bin/bash

function folder_creation {
  if [ ! -d $1 ]; then
    mkdir $1
  fi

  if [ ! -d "$1/fasta" ]; then
    mkdir "$1/fasta"
  fi

  if [ ! -d "$1/id" ]; then
    mkdir "$1/id"
  fi

  if [ ! -d "$1/afa" ]; then
    mkdir "$1/afa"
  fi
}

function exec_muscle {
  duf_file=$1
  name=$2
  output=$3
  echo "Processing $name"
  # Create the file with the correspondent DUF Name
  cat $duf_file | grep $name &> "$output/$name.txt"
  # It retries because sometimes it gets the error "HTTP Error 429: Too Many Requests"
  status=1
  while [ $status != 0 ]; do
    python3 jarvis.py raven.neo@gmail.com efetch_output.txt $name
    status=$?
    if [ $status == 1 ]; then
      echo "Processing $name failed. It's going to retry it"
    fi
  done
  # Move the files to their folders
  mv "${name}IDs.txt" "./$output/id"
  mv "${name}fasta.txt" "./$output/fasta"
  # Run Muscle3
  muscle -clwstrict -in "$output/fasta/${name}fasta.txt" -out "$output/afa/$name.afa"
}

function main {
  output="output"

  if [ $# != 1 ]; then
    echo "DUF File is needed"
    exit 1
  fi

  duf_file=$1

  # Extract unique DUF names
  duf_names=$(cat $duf_file |
              awk '{if ($0 ~ /Protein/) {next;} \
                    split($0,full_duf,","); \
                    split(full_duf[5], duf, " "); \
                    !seen[duf[1]]++;} \
                    END \
                    {for (elem in seen) print elem}')

  folder_creation $output

  for name in ${duf_names[@]}; do
    exec_muscle $duf_file $name $output
  done
}

main "$@"
