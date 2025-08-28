#!/usr/bin/env python

# cdhit cluster trimming script

import os
import re
from tqdm import tqdm # type: ignore  # noqa: F401

path_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(path_dir, "test_cluster.clstr")

with open(file_name, "r") as file:
    line_list = []
    for lines in file.readlines():
        line = lines.strip("\n")
        if line.startswith(">Cluster"):
            continue
        if "_g" in line:
            line_list.append(line)
    print(line_list)
 