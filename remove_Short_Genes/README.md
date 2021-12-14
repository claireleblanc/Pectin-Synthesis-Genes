## How to Use this code:

This filters a blast ouput file (file format 6) to only include target sequences with aligned with 80% or more of the query sequence. 

This program takes four arguments:
- -i: The input file (an output file from blast in format 6)
- -q: A tsv file where each line is the query sequence followed by the length of each sequence.
- -o: The output file to save the results. If this option is not included, the results will print to the screen.
- -p: The percentage of the query length that the alignment length must be greater than or equal to.  
- -names: If this option is included, only the target sequence name will be printed. Otherwise, the entire blastp line will be printed. 

### Examples:
python3 PycharmProjects/reu_project/remove_short_genes.py -i Downloads/RRTs_test.blastp -q Downloads/RRT_AT_length.tsv 

