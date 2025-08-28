#!/usr/bin/env python

# cdhit cluster trimming script

import os
# from tqdm import tqdm # type: ignore  # noqa: F401

path_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(path_dir, "trinity_95_cluster0.clstr")

with open(file_name, "r") as file:
    raw_data = file.read()

# Parse data

raw_data = raw_data.split(">Cluster")
raw_data = raw_data[1:]
cluster_list = []

for block in raw_data:
    cluster = set()
    raw_lines = block.split("\n")
    raw_lines = raw_lines[1:-1]
    for line in raw_lines:
        line = line.split("_g")
        line = line[1]
        line = line.split(".")
        line = line[0]
        cluster.add(line)
    cluster_list.append(cluster)    
# print(cluster_list)

# Process data 

cluster_new = []

for cur in cluster_list:
    int_found = False
    for cluster in cluster_new:
        cluster_int = cur.intersection(cluster)
        if cluster_int:
            cluster.update(cur)
            int_found = True
            break
    if not int_found:
        cluster_new.append(cur)
print(len(cluster_new))
    
        



# Print/store data 
# print("\n".join(raw_data))
