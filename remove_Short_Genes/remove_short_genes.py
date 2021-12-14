"""
Author: Claire LeBlanc
Last updated: 12/14/2021

Overview: Removes genes found in blast search that align with less than 80% of the query gene. 
"""
import csv
import argparse, textwrap
import sys

inPath = ""
outPath = ""
parser = argparse.ArgumentParser(add_help = True)
parser.add_argument('-i', action="store", dest="inPath", type=str, help="Path to fasta alignment file")
parser.add_argument('-q', action="store", dest="queryLength", type=str, help="Path to file containing query genes and associated lengths")
parser.add_argument('-o', action="store", dest="outPath", type=str, help="Path to output file (if not included, prints to screen)")
parser.add_argument('-names', action="store_true", default=False, dest="names", help="Will only print the target gene names")
parser.add_argument('-p', action="store", dest="percent", type=float, help="Percent of target sequence length that must be aligned")

args = parser.parse_args()

if args.inPath is not None: 
    inFile = open(args.inPath, "r")
else: 
    parser.print_usage()
    sys.exit("interestingRes: error: argument -i is required")

if args.queryLength is not None: 
    queryFile = open(args.queryLength, "r")
else: 
    parser.print_usage()
    sys.exit("interestingRes: error: argument -q is required")
if args.percent is not None: 
    percent = args.percent
else: 
    parser.print_usage()
    sys.exit("interestingRes: error: argument -p is required")
if args.outPath is not None: 
    outFile = open(args.outPath, "w+")
    sys.stdout = outFile

only_names = args.names

queryDict = {}

# Creates a dictionary where each query gene has its associated length
rq = csv.reader(queryFile, delimiter="\t", quotechar='"')
for row in rq:
    queryDict[(row[0])] = row[1]

# Calculates whether the alignment length is greater than 80% of the query length
ri = csv.reader(inFile, delimiter="\t", quotechar='"')
for row in ri:
    if (int(row[3]) > (int(queryDict[(row[0])])*percent)): 
        if only_names:
            print(row[1])
        else: 
            print(row)
