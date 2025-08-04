#!/usr/bin/env python

# Takes file with a list and returns dict with occurances of each element in list

import os
import collections

path_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(path_dir, "list_of_sequence_lengths.txt")

with open(file_name, "r") as file:
    values = file.read()
    # get rid of all commas
    vals = values.replace(",", " ")

    # convert numbers to floats
    seq_lengths = list(map(str, vals.split())) 

    # print(seq_lengths)

    # dict with lengths and occurances
    
    occ_lengths = collections.Counter(seq_lengths)
    # occ_len_sorted = dict(sorted(occ_lengths.items()))

    with open("occurances-lengths.txt", "w") as f:
        f.write(str(occ_lengths))
    

    # print(collections.Counter(seq_lengths))
    