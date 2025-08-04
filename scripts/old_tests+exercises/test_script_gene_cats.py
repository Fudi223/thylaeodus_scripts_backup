#!/usr/bin/env python 

# Testing script for categorizing and grouping genes. 

file_loc = "C:/Users/fdudi/OneDrive/Desktop/Master_Thesis_2025/thylaeodus-sharktankensis/analysis/2025-03_transcriptome_sampling/rosalind_tree.txt"
with open(file_loc, "r") as file:
    adjacency_list_raw = file.readlines()
    print(adjacency_list_raw)
    adjacency_list = " ".join(adjacency_list_raw)
    print(adjacency_list)
    