#!/usr/bin/python3

# import os

# path_dir = os.path.dirname(os.path.realpath(__file__))
# file_name = os.path.join(path_dir, "100000_lines_test.txt")

# search = "de:f:"
# search_len = len(search)

# lines_total = 0
# lines = []
# genes = []
# with open(file_name, "r") as file:
#     for line in file:
#         lines_total += 1
#         parts = line.split("\t")

#         is_relevant = False
#         num = 0

#         for part in parts:
#             if part.startswith(search):
#                 num = float(part[search_len:])
#                 if num < 0.02:
#                     is_relevant = True
#                     lines.append(line.rstrip())
#                     # print(line.rstrip())
#                     break

#         if is_relevant:
#             genes_combination = []
#             for part in parts:
#                 if part.startswith("NODE"):
#                     genes_combination.append(part)
#             genes_combination.append(num)
#             genes.append(tuple(genes_combination))

# for gene in genes:
#     print(gene)

# print("Lines total:", lines_total)
# print("Lines < 0.02:", len(lines))

import os

path_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(path_dir, "p_alignments.paf")

with open(file_name, "r") as file:
    alignment_list = file.readlines()
    alignments = " ".join(alignment_list)
    gene_list = []
    # gene_pairs = []
    columns = alignments.split("_")

    # extract genes (i.e. "g3") from the lines in the .paf file and add them to the gene_list
    for genes in columns:
        if genes.startswith("g"):
            gene_list.append(genes)
    # print(gene_list)

    # create list with genes from each line paired up, aka the genes with alignments
    # for pairs in range(0, len(gene_list), 2):
    #     pair = gene_list[pairs:pairs + 2]
    #     if len(pair) == 2:
    #         gene_pairs.append(pair)

    # alternative test
    gene_pairs = [['g1', 'g2'], ['g1', 'g3'], ['g3', 'g4'], ['g4', 'g5'], ['g5', 'g6'], ['g5', 'g7'], ['g6', 'g7'], ['g6', 'g8'], ['g7', 'g8']]

    print("These are my gene pairs:\n", gene_pairs)

    counter = 1
    cluster = {}
    for a, b in gene_pairs:
        if a not in cluster:
            cluster[a] = counter
            counter += 1
        if b not in cluster:
            cluster[b] = cluster[a]

    print("Clusters:\n", cluster)