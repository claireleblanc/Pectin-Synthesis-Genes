# How to use this code: 

The hmmsearch command produces a table that is not easily parsable using excel. This code extracts the names of genes identified in hmmsearch and creates a file containing these gene names. 

It takes two arguments: 
- `-i`: The input file, which comes from an hmmsearch using the --tblout format
- `-o`: The output file, where the gene names will be saved. If not included, results will be printed to the screen. 

### Example: 
`python2 code/hmmsearch_gene_names.py -i data/hmmsearch_results_1e-2.out -o data/hmmsearch_names.txt`
