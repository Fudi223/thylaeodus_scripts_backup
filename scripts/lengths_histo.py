#!/usr/bin/env python

# Takes file with sequence lengths as input and returns histogram of lengths and their occurances

import os
import matplotlib.pyplot as plt # type: ignore
# import numpy as np # type: ignore
# from tqdm import tqdm # type: ignore

path_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(path_dir, "list_of_sequence_lengths.txt")

with open(file_name, "r") as file:
    values = file.read()
    # get rid of all commas
    vals = values.replace(",", " ")

    # convert numbers to floats
    seq_lengths = list(map(float, vals.split()))   
    
    # use log10 to make the histogram slightly smaller and easier to look at
    x = seq_lengths
    binwidth = 8
    # histogram settings
    plt.hist(x, bins=100, color = "black", edgecolor='pink', linewidth=1.2)
    plt.title("Sequence lengths and occurances", fontsize=20)
    plt.xlabel("Lengths", fontsize=16)
    plt.ylabel("Occurances", fontsize=16)
    plt.show()