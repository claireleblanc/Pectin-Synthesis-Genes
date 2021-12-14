"""
Author: Claire LeBlanc
Last updated: 12/14/2021

Overview: The gene names in the cds sequence files are slightly different than the gene names in the protein files. 
This code specifically adds .1 after every Zosma gene, changes Potri.017G101301.1 to Potri.017G101300.1, and changes 
Potri.019G080901.1 to Potri.019G080900.1. These changes are necessary for faSomeRecords to work. 
"""
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
    if (line[-1] == '\n'): 
        if "Zosma" in line: 
            name = line[:-1] + ".1"
            print(name)
        elif line[:-1] == "Potri.017G101301.1":
            print("Potri.017G101300.1")
        elif line[:-1] == "Potri.019G080901.1":
            print("Potri.019G080900.1")
        else:
            print(line[:-1])
    else: 
        if "Zosma" in line: 
            name = line + ".1"
            print(name)
        elif line == "Potri.017G101301.1":
            print("Potri.017G101300.1")
        elif line == "Potri.019G080901.1":
            print("Potri.019G080900.1")
        else:
            print(line)
    j+=1
