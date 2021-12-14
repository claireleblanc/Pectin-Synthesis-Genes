import argparse, textwrap
import sys
import os

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
    outPath = args.outPath
else:
    outPath = "" 

lines = inFile.readlines()


j = 0

namesOld = ((lines[0].replace('\n', "")).replace('\r', "")).split('\t')

cols = len(namesOld)
rows = len(lines)
genes = [[0]*cols]*rows

names = [0]*len(namesOld)

for i in range(len(namesOld)):
    names[i] = outPath + namesOld[i] + "_names.txt"

for j in range(1, len(lines)):
    test = ((lines[j].replace('\n', "")).replace('\r', "")).split('\t')
    genes[j-1] = test

for k in range(len(names)): 
    with open(names[k], 'w+') as f: 
        for m in range (len(genes)):
            if ((genes[m][k] != "")): 
                print(genes[m][k], file = f)

for n in range(len(names)): 
    command1 = "python2 reference/faSomeRecords_CL_Updated.py -f reference/selected_species_062322_protein.fa -l " + names[n] + " -o " + outPath + namesOld[n] + ".fa -k"
    os.system(command1)
    
    command2 = "mafft --quiet " + outPath + namesOld[n] + ".fa > " + outPath + namesOld[n] + ".fa.mafft.align"
    os.system(command2)
    
    command3 = "python3 reference/interestingRes_v2.py -i " + outPath +  namesOld[n] + ".fa.mafft.align -o " + outPath + namesOld[n] + "_results.txt -aa"

    #command3 = "python3 reference/interestingRes_v2.py -i Final_Data/RRTs/clade_analysis/" + namesOld[n] + ".fa.mafft.align -aa"
    
    with open(names[n], 'r') as f: 
        clade_names = f.readlines()
        for p in range(len(clade_names)):
            gene = clade_names[p]
            if ("AT" in gene) | ("VIT" in gene) | ("Glyma" in gene) | ("Potri" in gene) | ("Solyc" in gene): 
                command3 = command3 + " -d " + str(p + 1)
            if ("Zosma" in gene) | ("Phequ" in gene) | ("Dioal" in gene) | ("Asparagus" in gene): 
                command3 = command3 + " -m " + str(p + 1)
            if ("ELECO" in gene) | ("Zm" in gene) | ("Sevir" in gene) | ("LOC" in gene) | ("Bradi" in gene) | ("HORVU" in gene): 
                command3 = command3 + " -g " + str(p + 1)
            if ("Aco" in gene) | ("KAF" in gene): 
                command3 = command3 + " -c " + str(p + 1)
    os.system(command3)
