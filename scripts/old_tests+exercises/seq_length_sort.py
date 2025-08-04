#!/usr/bin/env python

# Counts lengths of sequences in any given FASTA file and sorts them by length

import os
from tqdm import tqdm # type: ignore

path_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(path_dir, "transcripts.fasta")
print("Loading file...")

with open(file_name, "r") as file:

    lines = file.readlines()
    seq_parts = " ".join(lines)
    # print(lines)
    seq_lengths = {}
    trans_seqs = seq_parts.split()
    # print(trans_seqs)

    
    # for linies in trans_seqs:
    #     if linies.startswith(">") and linies.endswith("\n"):
    #         print(linies)

    print("Creating dictionary with sequence names and lenghts...")
    for nukes in tqdm(trans_seqs):
        # print(nukes)
        if nukes.startswith(">"):
            seq_length = 0
            a_counter = 0
            t_counter = 0
            g_counter = 0
            c_counter = 0
            n_counter = 0
            seq_names = nukes
            seq_lengths[seq_names] = 0
        for atgc in nukes: 
            if atgc == "A":
                a_counter += 1
            if atgc == "T":
                t_counter += 1
            if atgc == "G":
                g_counter += 1
            if atgc == "C":
                c_counter += 1
            if atgc == "N":
                n_counter += 1
            seq_length = a_counter + t_counter + g_counter + c_counter + n_counter
        seq_lengths.update({seq_names: seq_length})
        only_lengths = list(seq_lengths.values())

    print("Number of Adenine occurances:", a_counter)
    print("Number of Thymine occurances:", t_counter)
    print("Number of Guanine occurances:", g_counter)
    print("Number of Cytosine occurances:", c_counter)
    print("Number of indet. basecalls:", n_counter)
    print("Total lenght of the sequence:", seq_length)

    with open ("lengths_only.txt", "w") as f:
        f.write(str(only_lengths))