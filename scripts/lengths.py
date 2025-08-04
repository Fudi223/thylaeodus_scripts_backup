#!/usr/bin/env python

# Get the lengths only from the file with the sequences and lengths

import os
from tqdm import tqdm # type: ignore

path_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(path_dir, "transcripts.fasta")
print("Loading file...")

with open(file_name, "r") as file:
    lines = tqdm(file.readlines())
    longs = []

    # Extract only the lines with the titles of the sequences

    for numbs in lines:
        if numbs.startswith(">"):
            longs.append(numbs)

    # Split the sequence name apart and extract the length number which is always at position [3]

    print("Extracting lengths of sequences...")
    lengies = tqdm([parts.split("_")[3] for parts in longs])
    length_numbers = list(map(int, lengies))
    # print(length_numbers)
    
    # Save as a list of sequence lengths for further processing

    with open("list_of_sequence_lengths.txt", "w") as f:
        f.write(str(length_numbers))

    print("Done!")