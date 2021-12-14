"""
Author: Claire LeBlanc
Last updated: 12/14/2021

Overview: Removes genes with a more significant GT24 domain than GT8 to prevent
misidentification of GT24 genes as GT8 genes. 
"""

import argparse, textwrap
import sys

inPath = ""
outPath = ""
parser = argparse.ArgumentParser(add_help = True)
parser.add_argument('-GT8', action="store", dest="GT8Path", type=str, help="Path to fasta alignment file")
parser.add_argument('-GT24', action="store", dest="GT24Path", type=str, help="Path to file containing query genes and associated lengths")
parser.add_argument('-o', action="store", dest="outPath", type=str, help="Path to output file (if not included, prints to screen)")

args = parser.parse_args()

if args.GT8Path is not None: 
    GT8File = open(args.GT8Path, "r")
else: 
    parser.print_usage()
    sys.exit("interestingRes: error: argument -i is required")

if args.GT24Path is not None: 
    GT24File = open(args.GT24Path, "r")
else: 
    parser.print_usage()
    sys.exit("interestingRes: error: argument -q is required")
if args.outPath is not None: 
    outFile = open(args.outPath, "w+")
    sys.stdout = outFile

GT24Dict = {}

GT24lines = GT24File.readlines()
j = 0

# Creates a dictionary containing each GT24 gene and the associated significance of the GT24 domain
while (j < len(GT24lines)):
        line = GT24lines[j]
        if ("#" not in line): 
            words = line.split()
            GT24Dict[words[2]] = float(words[4])    
        j+=1

# Uses the earlier dictionary to compare the significance of GT8 genes with the corresponding GT24 significance
# If there is no GT24 domain, than the gene is automatically included
GT8lines = GT8File.readlines()
i = 0
while (i < len(GT8lines)): 
    line = GT8lines[i]
    if ("#" not in line): 
        words = line.split()
        if GT24Dict.has_key(words[2]): 
            Eval = GT24Dict[words[2]]
            test = Eval > float(words[4])
            if(test): 
                print(words[2])
        else:
            print(words[2])
    i+=1
