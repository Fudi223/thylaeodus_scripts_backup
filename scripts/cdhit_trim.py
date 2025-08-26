#!/usr/bin/env python

# cdhit cluster trimming script

import os
from tqdm import tqdm # type: ignore  # noqa: F401

path_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(path_dir, "test_cluster.clstr")

with open(file_name, "r") as file:
    blocki = ()
    for blocks in file.readlines():
        if blocks[0] == ">":
            print(blocki)