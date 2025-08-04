#!/usr/bin/env python

# Translate DNA sequences into protein sequences 

import os
from tqdm import tqdm # type: ignore

path_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(path_dir, "testing_sequence.txt")

with open(file_name, "r") as file:
    sequence1 = file.read()
    sequence2 = sequence1.replace("\n","")
    seqies = []
    # print(sequence2)

    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
            }

    peptide = ""
    for start in range(0, len(sequence2), 3):
        codon = sequence2[start:start+3]
        aminoacid = table[codon]
        if aminoacid == "Stop":
            break
        peptide += aminoacid
    print(peptide)
