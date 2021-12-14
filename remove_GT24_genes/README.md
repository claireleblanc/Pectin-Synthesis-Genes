# How to use this code: 

The CAZy GT8 domain is very similar to the GT24 domain, and they are often misidentified for one another. This code takes two file produced after running hmmscan (with --tblout option), one using Glyco_transf_8 profile database and one using Glyco_transf_24 profile database, and only only returns genes where the GT8 domain was more significant than the GT24 domain. 

This script takes three arguments: 
- `-GT24`: The file produced from runnning hmmscan with Glyco_transf_24 profile database
- `-GT8`: The file produced from running hmmscan with Glyco_trasf_8 profile databse
- `-o`: The output file to save the results. If not included, results will print to the screen

### Example: 
`python2 reference/remove_GT24.py -GT24 Final_Data/GAUT_GATL/identifying_genes/hmmscan_results_GT24_1e-2.out -GT8 Final_Data/GAUT_GATL/identifying_genes/hmmscan_results_GT8_1e-2.out -o Final_Data/GAUT_GATL/identifying_genes/GT8_protein_genes.txt`
