#!/usr/bin/python3
import os

path_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(path_dir, "rosalind_tree.txt")

with open(file_name, "r") as file:
    # read first line, nodes count
    nodes_count = int(file.readline().rstrip())
    # file.seek(os.SEEK_SET)

    # create list for edges
    edges_count = 0
    # read remaining lines, edge definitions
    # for line in file: # also works
    while line := file.readline().rstrip():
        edges_count += 1

    print("Nodes Count:", nodes_count)
    print("Edges Count:", edges_count)
    print("Edges to add:", nodes_count - 1 - edges_count)