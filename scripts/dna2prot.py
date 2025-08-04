#!/usr/bin/env python


import os
from tqdm import tqdm # type: ignore

path_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(path_dir, "transcripts.fasta")
print("Loading file...")

with open(file_name, "r") as file:
    lines = tqdm(file.readlines())
    seq_parts = " ".join(lines)
    print(seq_parts)


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
    
    # seq_list = seq_parts[0]
    # peptide = ""
    # for start in range(0, len(seq_list), 3):
    #     codon = seq_list[start:start+3]
    #     aminoacid = table[codon]
    #     if aminoacid == "Stop":
    #         break
    #     peptide += tqdm(aminoacid)
    # # print(codon, "corresponds to", aminoacid)

    # print(peptide)