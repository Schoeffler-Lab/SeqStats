# SeqStats
This repository contains a set of python scripts for calculating and visualizing amino acid frequencies in sets of protein sequences. 

# Instructions
NOTE: These instructions assume you have a small amount of familiarity with the command line. You don't need much familiarity with python.
1) Download the contents of this repository and place the files in thier own directory.
2) Copy your unaligned sequence files (FASTA format only) into the directory.

## Run Counter Catalog
3) Edit the counter_catalog.py script to accept one of your sequence files and output a .csv file with a unique name. (You can do this by opening the script in vi or TextEdit and editing the indicated lines of code.)
4) Run counter_catalog.py by typing 'python counter_catalog.py' at your command line prompt.
5) Repeat steps 3 and 4 for all of your sequence sets. (This code package was build assuming that you have sets of homologous sequences from psychrophiles, meosphiles and thermophiles.)
6) The script will produce a csv file containing counts and frequencies for all twenty amino acids. It will also produce summary statistics (average, standard deviation, etc.)
   
## Run Stat Catalog
7) Decide which pairs you want to investigate for statistical significance.
8) Edit the stat_catalog.py script to accept two of the output files produced by counter_catalog.py (say, one for thermophiles and one for psychrophiles.) You should also edit the output file name to give the output file a unique name. 
9) It is crucial that you do not edit the counter_catalog.py output in any way.
10) Run stat_catalog.py by typing 'python stat_catalog.py' at your command line prompt.
11) The script will run a two-tailed, heterscedastic t-test for the two sets your specify, for all twenty amino acids (raw counts and frequency) and for sequence length. It will output a csv file containing the t-test value and the P-value.

## Run Quicker-Hist
12) NOTE: This script assumes that you have run counter_catalog.py on three sets of homologous sequences.
13) Edit quickerhist.py to read in your three counter_catalog.py output files.
14) If desired, edit the "my protein" tag so that your urput files all have a custom prefix.
15) If desired, edit the legend labels to reflect the three sequence sets you are investigating.
16) Run quickerhist.py by typing 'python quickerhist.py' at your command line prompt.
17) The program will automatically create and save normalized histograms and boxen plots comparing your three data sets. 
