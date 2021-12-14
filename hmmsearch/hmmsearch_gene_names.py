"""
Author: Claire LeBlanc
Last updated: 12/14/2021

Overview: Creates file with the names of genes identified with hmmsearch. 
"""

import csv
import argparse, textwrap
import sys

inPath = ""
outPath = ""
parser = argparse.ArgumentParser(add_help = True)
parser.add_argument('-i', action="store", dest="inPath", type=str, help="Path to fasta alignment file")
parser.add_argument('-o', action="store", dest="outPath", type=str, help="Path to output file (if not included, prints to screen)")

args = parser.parse_args()

if args.inPath is not None: 
    inFile = open(args.inPath, "r")
else: 
    parser.print_usage()
    sys.exit("interestingRes: error: argument -i is required")

if args.outPath is not None: 
    outFile = open(args.outPath, "w+")
    sys.stdout = outFile

lines = inFile.readlines()
j = 0
while (j < len(lines)): 
    line = lines[j]
    if "#" not in line:
        i = 0
        name = ""
        while ((line[i] != ' ') & (i < len(line))): 
            name = name + line[i]
            i+=1
        print(name)
    j+=1
