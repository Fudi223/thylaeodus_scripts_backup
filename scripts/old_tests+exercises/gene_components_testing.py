#!/usr/bin/env python

# Script for testing out formatting of gene data lines and assigning genes to components

import os


path_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(path_dir, "p_alignments.paf")

with open(file_name, "r") as file:
    alignment_list = file.readlines()
    alignments = " ".join(alignment_list)
    gene_list= ["g1", "g2", "g1", "g3", "g3", "g4", "g5", "g6", "g5", "g7", "g6", "g7"]
    gene_pairs = []
    test_list = []
    components = {}
    component_counter = 1
    columns = alignments.split("_")
    # for gene in columns:
    #     if gene.startswith("g"):
    #         gene_list.append(gene)
    # print("These are my genes: ",gene_list)

    for pairs in range(0, len(gene_list), 2):
        pair = gene_list[pairs:pairs+2]
        if len(pair) == 2:
            gene_pairs.append(pair)
    print("These are gene pairs: ","\n\n", gene_pairs, "\n\n")

    for gene_p in gene_pairs:
        list_of_genes = " ".join(gene_p)
        components[list_of_genes] = component_counter
        if components[list_of_genes] == list_of_genes:
            continue
        if components[list_of_genes] != list_of_genes:
                component_counter += 1
                components.update()
    print("These are genes with their respective component number: ","\n\n",components, "\n\n")

