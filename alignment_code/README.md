## Overview: 

interestingRes_v2.py analyzes the alignments as described bellow. 
clade_analysis.py and clade_analysis_2.py are two wrapper programs that allow running of these analyses in bulk. They are also described in more detail below. 

## How to use interestingRes_v2.py: 

Given a sequence alignment, this code will identify locations in the alignment where groups are different from eachother. It is configured to compare grasses, non-grass commelinids, non-commelinid monocots, and dicots, but it could easily be configured to compare different groups. 

To run this code, download the python file and save it somewhere on your device. 
- In order for the code to run, you need to tell it which genes belong in each group. 
- Each gene is numbered based on its position in the alignment. The first gene in the alignment is 1, the second gene is 2, etc. There are multiple ways to identify genes as belonging to a specific group. 
- If genes from the same group are next to eachother, you can use the range options (-gr, -cr, -mr, -dr). 
  -  For example, -gr 2 7 means that the second, third, fourth, fifth, sixth, and seventh genes are all grasses. 
  -  Similarly, -dr 1 3 means that the first, second and third genes are all dicots. 
-  Additionally, you can label a single gene as a member of a specific group using the single gene options (-g, -c, -m, -r)
-   For example, -c 5 means that the fifth gene is a non-grass commelinid. 
-  There can be multiple (or none) of each type of gene grouping options. 
  - You could have multiple -gr options, and no -m or -dr options.
- If a gene is not labeled as one of the four groups, it will not be included in the analysis. 
- If a gene is labeled as multiple groups, the analysis will run as if there are duplicate genes, one in each group.   

There are a few other options in the code. 
- -o: An output file to write the results. If not included, the results will print to the screen. 
- -aa: If included, the amino acids at the identified residues will be printed in the output file. Otherwise, they will not be printed.
- -struct: If a partial structure has been predicted for a gene, then this option will check if the identified alignment sequence position is within the structure. 
  - Use -ss to identify the starting postition of the predicted structure within the alignment, and use -se to identify the ending position.  

### Example

`python3 interestingRes.py -i "../../Downloads/alignments_3/clade1_3.fa.mafft.align" -aa -gr 3 15 -c 16 -cr 1 2 -mr 17 24` 

## How to clade_analysis.py 
This code runs the alignment analysis for multiple clades, but does not include the structure analysis. To run this code, you need: 
- i: a file where each column header is the clade name, and then below that column is a list of all the genes in that clade (example in this folder titled all_GAUT_clade_names.txt)
- -o: an output path (the folder where you want the output files to be saved) 

### Example

`python3 reference/clade_analysis.py -i Final_Data/RRTs/clade_analysis/all_RRT_clade_names.txt -o Final_Data/RRTs/clade_analysis/`

## How to clade_analysis_2.py 
This code runs the alignment analysis for multiple clades, and includes the structure analysis. To run this code, you need: 
- -i: a file where each column header is the clade name, and then below that column is a list of all the genes in that clade (example file in this folder titled all_GAUT_clade_names.txt)
- -o: an output path (the folder where you want the output files to be saved) 
- -s: a file containing the structural information. Specifically, the first column should be the clade name (matching the clade name in the first file exactly), the second column should be a representative protein from that clade for which a partial structure has been predicted, the third column should be the first five amino acids of the predicted structure, and the last column should be the last five amino acids of the predicted structure (example file in this folder titled GAUT_struct_data.txt)

### Example

`python3 reference/clade_analysis_2.py -i Final_Data/GAUT_GAL/clade_analysis/GAUT/all_GAUT_clade_names.txt -o Final_Data/GAUT_GATL/clade_analysis/GAUT/ -s Final_Data/GAUT_GATL/clade_analysis/GAUT/GAUT_struct_data.txt`

