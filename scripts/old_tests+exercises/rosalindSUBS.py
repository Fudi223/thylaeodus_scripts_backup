#!/usr/bin/env python

# Rosalind Exercise "cons"

# Input : Collection of at most 10 DNA strings of equal lenght in FASTA format
# Return : Consensus string and profile matrix for the collection 

file_loc = "C:/Users/fdudi/OneDrive/Desktop/Master_Thesis_2025/thylaeodus-sharktankensis/analysis/2025-03_transcriptome_sampling/rosaFasta.txt"

with open(file_loc, "r") as file:
    for lines in file: 
        if lines.startswith(">"):
           pass
        else:
            print(lines.strip("\n"))
    