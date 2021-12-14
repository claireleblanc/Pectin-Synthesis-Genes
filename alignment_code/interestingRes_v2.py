"""
Author: Claire LeBlanc
Last updated: 12/14/2021

Overview: Compares grass, commelinid, monocot, and dicot genes within an alignment, 
and identifies amino acid residues where the residue is the same within a group, and 
different than the other group(s), which could potentially hint at important amino acids 
and/or differing evolutionary pressures. 
"""

import argparse, textwrap
import sys

grass_list = []
comm_list = []
mono_list = []
di_list = []
grass_comm_list = []
grass_comm_mono_list = []
comm_mono_di_list = []
mono_di_list = []

description = ""

## HELPER FUNCTIONS

# Creates a list of amino acids in each group at a specific residue
def initalize_groups(list, i):

    amino_acid = list[i]
        
    for j in grass:
        grass_list.append(amino_acid[j -1])
        grass_comm_list.append(amino_acid[j -1])
        grass_comm_mono_list.append(amino_acid[j -1])
    
    for j in comm: 
        comm_list.append(amino_acid[j-1])
        grass_comm_list.append(amino_acid[j-1])
        grass_comm_mono_list.append(amino_acid[j-1])
        comm_mono_di_list.append(amino_acid[j-1])

    for j in monocot: 
        mono_list.append(amino_acid[j-1])
        grass_comm_mono_list.append(amino_acid[j-1])
        comm_mono_di_list.append(amino_acid[j-1])
        mono_di_list.append(amino_acid[j-1])

    for j in dicot: 
        di_list.append(amino_acid[j-1])
        comm_mono_di_list.append(amino_acid[j-1])
        mono_di_list.append(amino_acid[j-1])

# Creates the final table and calls the test funcion to run the analysis
def make_output_table(i):
    g_label = ""
    cmd_label = ""
    c_label = ""
    md_label = ""
    gcm_label = ""
    d_label = ""
    description = ""
    
    if ((i+1 < struct_start) | (i + 1 > struct_end)):
        location = "outside of modeled protein"
    else: 
        location = "within modeled protein"
    
    if ((len(grass_list) > 0) & (len(comm_mono_di_list) > 0)):
        g_label = test(grass_list, comm_mono_di_list, "grasses")
        cmd_label = test(comm_mono_di_list, grass_list, "non-grasses")
    
    if ((len(grass_comm_list) > 0) & (len(mono_di_list) > 0)):
        c_label = test(grass_comm_list, mono_di_list, "commelinids")
        md_label = test(mono_di_list, grass_comm_list, "non-commelinids")
    
    if ((len(grass_comm_mono_list) > 0) & (len(di_list) > 0)):
        gcm_label = test(grass_comm_mono_list, di_list, "monocots")
        d_label = test(di_list, grass_comm_mono_list, "dicots")
    
    description = g_label+ cmd_label + c_label + md_label + gcm_label + d_label 

    if (len(description) > 0):
        if (include_aa & include_struct):
            print(str(i + 1) + "\t" + description + "\t" + str(grass_list) + "\t" + str(comm_list) + "\t" + str(mono_list) + "\t" + str(di_list) + "\t" + location)
        elif (include_aa):
            print(str(i + 1) + "\t" + description + "\t" + str(grass_list) + "\t" + str(comm_list) + "\t" + str(mono_list) + "\t" + str(di_list))
        elif (include_struct): 
            print(str(i + 1) + "\t" + description + "\t" + location)
        else: 
            print(str(i + 1) + "\t" + description)
            
# Takes in the amino acids in two groups (i.e. grasses and non-grasses) and runs a variety of tests
def test(list1, list2, name):
    tag = ""
    if ( (all_equal (list1)) & (not_equal (list2, list1))): 
        tag += (name + " are equal | ")
    
    if (all_hydrophobic(list1) & no_hydrophobic(list2)):
        tag += (name + " are hydrophobic | ")
        
    if (all_positive(list1) & no_positive(list2)):
        tag += (name + " are positive | ")  
    
    if (all_negative(list1) & no_negative(list2)):
        tag += (name + " are negative | ")
    
    if (all_polar_uncharged(list1) & no_polar_uncharged(list2)):
        tag += (name + " are polar uncharged | ")
    
    return tag 

# Tests whether all the amino acids are the same
def all_equal(list):
    for c in list:
        if (list[0] == '-'):
            return False
        if (c != list[0]):
            return False
    return True

# Tests whether none of the the amino acids in one list are in the other
def not_equal(listA, listB): 
    for c in listA:
        if (len(listB) > 0) & ((c == listB[0]) & (c != '-')):
            return False
    return True

# Tests whether all the amino acids are hydrophobic
def all_hydrophobic(list): 
    for c in list:
        if ((c != 'A') & (c != 'V') & (c != 'L') & (c != 'I')  & (c != 'P') & (c != 'F') & (c != 'M') & (c !='W') | (c == '-')):
            return False
    return True

# Tests if none of the amino acids are hydrophobic
def no_hydrophobic(list):
    for c in list:
        if ((c == 'A') | (c == 'V') | (c == 'L') | (c == 'I') | (c == 'P') | (c == 'F') | (c == 'M') | (c =='W')): 
            return False
    return True

# Tests if all the amino acids are positive
def all_positive(list): 
    for c in list: 
        if ((c != 'R') & (c != 'H') & (c != 'K') | (c == '-')): 
            return False
    return True

# Tests if none of the amino acids are positive
def no_positive(list): 
    for c in list: 
        if ((c == 'R') | (c == 'H') | (c == 'K')): 
            return False
    return True

# Tests is all the amino acids are negative
def all_negative(list):
    for c in list: 
        if ((c != 'D') & (c != 'E') | (c == '-')): 
            return False
    return True

# Tests if none of the amino acids are negative
def no_negative(list): 
    for c in list: 
        if ((c == 'D') | (c == 'E')): 
            return False
    return True

# Tests if all the amino acids are polar uncharged
def all_polar_uncharged(list): 
    for c in list:
        if ((c != 'S') & (c != 'T') & (c != 'N') & (c != 'Q') | (c == '-')): 
            return False
    return True

# Tests if none of the amino acids are polar uncharged
def no_polar_uncharged(list): 
    for c in list: 
        if ((c == 'S') | (c == 'T') | (c == 'N') | (c == 'Q')):
            return False
    return True

# Code for processing and reading in command line arguments
inPath = ""
outPath = ""
parser = argparse.ArgumentParser(add_help = True)
parser.add_argument('-i', action="store", dest="inPath", type=str, help="Path to fasta alignment file")
parser.add_argument('-o', action="store", dest="outPath", type=str, help="Path to output file (if not included, prints to screen)")
parser.add_argument('-aa', action="store_true", default=False, dest="incl_aa", help="Will include amino acids at residue in output")
parser.add_argument('-gr', nargs=2, action="append", dest="grass_range", type=int, help="Start and end of group of grass genes") 
parser.add_argument('-cr', nargs=2, action="append", dest="comm_range", type=int, help="Start and end of group of non-grass commelinid genes") 
parser.add_argument('-mr', nargs=2, action="append", dest="mono_range", type=int, help="Start and end of group of non-commelinid monocot genes") 
parser.add_argument('-dr', nargs=2, action="append", dest="dicot_range", type=int, help="Start and end of group of dicot genes") 
parser.add_argument('-g', action="append", dest="grass", type=int, help="Location of a grass gene")
parser.add_argument('-c', action="append", dest="comm", type=int, help="Location of a non-grass commelinid gene")
parser.add_argument('-m', action="append", dest="mono", type=int, help="Location of a non-commelinid monocot gene")
parser.add_argument('-d', action="append", dest="dicot", type=int, help="Location of a dicot gene")
parser.add_argument('-struct', action="store_true", default=False, dest="incl_struct", help="Will include whether of not is in predicted structure")
parser.add_argument('-sr', nargs=2, action="store", dest="struct_range", type=int, help="Start and end of predicted structure")

args = parser.parse_args()

if args.inPath is not None: 
    inFile = open(args.inPath, "r")
else: 
    parser.print_usage()
    sys.exit("interestingRes: error: argument -i is required")
if args.outPath is not None: 
    outFile = open(args.outPath, "w+")
    sys.stdout = outFile

if args.grass is not None: 
    grass = args.grass
else: 
    grass = []
if args.comm is not None: 
    comm = args.comm 
else: 
    comm = []
if args.mono is not None: 
    monocot = args.mono
else: 
    monocot = []
if args.dicot is not None: 
    dicot = args.dicot
else: 
    dicot = []

if args.grass_range is not None: 
    i = 0
    grass_range = args.grass_range 
    while (i < len(grass_range)):
        start = grass_range[i][0]  
        end = grass_range[i][1]
        j = start
        while (j <= end):
            grass.append(j)
            j +=1
        i +=1

if args.comm_range is not None: 
    i = 0
    comm_range = args.comm_range 
    while (i < len(comm_range)):
        start = comm_range[i][0]  
        end = comm_range[i][1]
        j = start
        while (j <= end):
            comm.append(j)
            j +=1
        i +=1

if args.mono_range is not None: 
    i = 0
    mono_range = args.mono_range 
    while (i < len(mono_range)):
        start = mono_range[i][0]  
        end = mono_range[i][1]
        j = start
        while (j <= end):
            monocot.append(j)
            j +=1
        i +=1

if args.dicot_range is not None: 
    i = 0
    dicot_range = args.dicot_range 
    while (i < len(dicot_range)):
        start = dicot_range[i][0]  
        end = dicot_range[i][1]
        j = start
        while (j <= end):
            dicot.append(j)
            j +=1
        i +=1

include_struct = args.incl_struct
include_aa = args.incl_aa

if args.struct_range is not None: 
    struct_start = args.struct_range[0]
    struct_end = args.struct_range[1]
else: 
    if (include_struct):
        parser.print_usage()
        sys.exit("interestingRes: error: argument -sr is required when struct is true")
    else:
        struct_start = 0
        struct_end = 0
 
# Reading the input file and changing it into a more parsable format 
first = 0

lines = inFile.readlines()

j = 0
big_list = []

while (j < len(lines)): 
    i = 0
    if not (lines[j][0] == ">"):
        if (first == 0):
            while (not (lines[j][0] == ">")):
                small_list = [lines[j][i]]
                big_list.append(small_list)
                if ((i + 2) == len(lines[j])):
                    j +=1
                    i = 0
                else: 
                    i+=1 
            first = 1
        else:
            k = 0
            while (not (lines[j][0] == ">")):
                big_list[k].append(lines[j][i])
                if ((i + 2) == len(lines[j])):
                    if ((j + 1) < len(lines)):
                        j +=1
                        k += 1
                        i = 0
                    else: 
                        break
                else: 
                    i+=1
                    k += 1 
    j+=1

coord = 0

# Printing the headers for the file
if (include_aa & include_struct):
    print("coordinate\tdescription\tgrass amino acids\tnon-grass commelinid amino acids\tnon-commelinid monocot amino acids\tdicot amino acids_list\tlocation in structure")
elif (include_aa):
    print("coordinate\tdescription\tgrass amino acids\tnon-grass commelinid amino acids\tnon-commelinid monocot amino acids\tdicot amino acids_list")
elif (include_struct):
    print("coordinate\tdescription\tlocation in structure") 
else: 
    print("coordinate\tdescription")

# Going through the alignment and testing each position
while (coord < len(big_list)):
    grass_list = []
    comm_list = []
    mono_list = []
    di_list = []
    grass_comm_list = []
    grass_comm_mono_list = []
    comm_mono_di_list = []
    mono_di_list = []
    
    initalize_groups(big_list, coord)
    make_output_table(coord)
    coord += 1
    
