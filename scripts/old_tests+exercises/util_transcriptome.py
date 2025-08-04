#!/usr/bin/env python

# library of functions for transcriptome processing and analyzing

# returns input file with columns formatted



def read_input(filepath):
        with open(filepath, "r") as infile:
            lines = infile.readlines()
            stripped = " "
            for line in lines:
                stripped.append(line.split())
        return stripped



