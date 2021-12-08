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
while (j < len(lines)-1):
    line = lines[j]
    if "Zosma" in line: 
        name = line[:-1] + ".1"
        print(name)
    elif line[:-1] == "Potri.017G101301.1":
        print("Potri.017G101300.1")
    elif line[:-1] == "Potri.019G080901.1":
        print("Potri.019G080900.1")
    else:
        print(line[:-1])
    j+=1
print(line)
