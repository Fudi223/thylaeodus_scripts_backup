#!/usr/bin/env python

# Pairing genes and categorizing genes

import os
from tqdm import tqdm # type: ignore

path_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(path_dir, "t-asm20_SD5%_SC.txt")

with open(file_name, "r") as file:
    alignment_list = file.readlines()
    alignments = " ".join(alignment_list)
    gene_list= []
    gene_pairs = []
    columns = alignments.split("_")

    # extract genes (i.e. "g3") from the lines in the .paf file and add them to the gene_list
    for genes in columns:
        if genes.startswith("g"):
            gene_list.append(genes)
    # print(gene_list)
    
    print('creating list with genes...') #from each line paired up, aka the genes with alignments
    for pairs in tqdm(range(0, len(gene_list), 2)):
        pair = gene_list[pairs:pairs+2]
        if len(pair) == 2:
            gene_pairs.append(pair)
    #print("These are my gene pairs","\n\n",gene_pairs)

    
    # create a dictionary with the genes as keys and values set to "0"
    components = {el:0 for el in gene_list}
    # print(components)
    
    component_counter = 1
    gene_components = {}
    print('parsing gene pairs...')
    for gene_1, gene_2 in tqdm(gene_pairs):
        if gene_1 == gene_2:
             continue
        if gene_1 not in gene_components:
            gene_components[gene_1] = component_counter
            component_counter += 1
        if gene_2 not in gene_components:
            gene_components[gene_2] = gene_components[gene_1]


    print("Clusters:\n", gene_components)




    
    
