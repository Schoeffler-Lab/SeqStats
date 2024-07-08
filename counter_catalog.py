# Allyn J. Schoeffler, PhD
# Loyola University New Orleans
# See MIT license for usage and permissions
# Edit file names as indicated below.

#package imports DO NOT EDIT
import numpy
import matplotlib.pyplot
import pandas

########
#Edit below for your file names:

# Below, replace "your_unaligned_seqs.fa" with the FASTA format file
# containing the unaligned sequences you wish to analyze
# Replace myoutput.csv with a unique file name in whihc to store our output statistics.
 
seqfiles = open('my_seqs.fa', 'r')
output_file_name = 'my_output.csv'
########

#### Don't alter anything below this line unless you are an experience python coder

# This function will create a list of lists.
# Each sub-list comprises an element for each line in the sequence entry.

def sequence_splitter(seqfiles):
	list_of_seqlists = []
	for line in seqfiles:
		if '>' in line:
			indseqlist = []
			indseqlist.append(line)
		if '>' not in line:
			indseqlist.append(line)
		if '>' in line and indseqlist != []:
			list_of_seqlists.append(indseqlist)
	return list_of_seqlists
		

# This function will take each sequence list from the list of lists
# and turn it into a single two-element list.
# The first element will be a string containing the FASTA header..
# The second element will be a list of individual amino acids.
# This process strips new-line characters from the sequence entry.

def indseq_list(list_of_seqs, seq_index):

	# grab the desired sequence
	starter_sequence = list_of_seqs[seq_index]

	# turn the lines into a list of amino acids
    # It begins with index 1, because index 0 is the header
	number_of_lines = len(starter_sequence)
	counter = 1
	seq_list = []
	while counter < number_of_lines:
		stripped_line = starter_sequence[counter].rstrip('\n')
		line_list = list(stripped_line)
		seq_list = seq_list + line_list
		counter = counter + 1
	
	name_and_seq_list = [starter_sequence[0], seq_list]	
    
    # returns a single two-component list comprising a sequence name and a list of amino acids.
	return name_and_seq_list


# The command below calls the function to create the list of lists

full_seq_list = sequence_splitter(seqfiles)

# The code below creates a dictionary of all sequences from the input FASTA file

seq_dictionary = {}
number_of_sequences = len(full_seq_list)
seq_counter = 0
while seq_counter < number_of_sequences:
	seq_name_aa_list = indseq_list(full_seq_list,seq_counter)
	seq_dictionary[seq_name_aa_list[0]] = seq_name_aa_list[1]
	seq_counter = seq_counter + 1


# Below, we use the sequence dictionary to create a list of FASTA headers (aka sequence names or sequence ids)

seqname_list = []
for sequence in seq_dictionary:
    seqname = sequence.rstrip('\n')
    seqname_list.append(seqname)

# Below, we create a dataframe in which the index  is the name of the sequence (FASTA header)
# and the first column is the FASTA header as well.

df = pandas.DataFrame({'name':seqname_list}, index = seqname_list)

# Below, we use the sequence dictionary to calculate the length of each sequence.
# We will store these sets of values in pandas Series objects, with the FASTA headers as the index.
# We then add these values to the data frames using the FASTA headers as the index.

seqname_list2 = []
total_length_list = []
for sequence in seq_dictionary:
    total_length = len(seq_dictionary[sequence])
    seqname2 = sequence.rstrip('\n')
    total_length_list.append(total_length)
    seqname_list2.append(seqname2)

s_length = pandas.Series(total_length_list, index = seqname_list2)
df['length'] = s_length.values

    
the_20_aas = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V']

for aa in the_20_aas:
    seqname_list3 = []
    aa_count_list = []
    aa_freq_list = []
    for sequence in seq_dictionary:
        total_length = len(seq_dictionary[sequence])
        seqname3 = sequence.rstrip('\n')
        seqname_list3.append(seqname3)
        aa_count = seq_dictionary[sequence].count(aa)
        aa_count_list.append(aa_count)
        aa_freq = aa_count / total_length
        aa_freq_list.append(aa_freq)
    s_aa_count = pandas.Series(aa_count_list, index = seqname_list3)
    s_aa_freq = pandas.Series(aa_freq_list, index = seqname_list3)
    df[aa] = s_aa_count.values
    freqname = aa + ' frequency'
    df[freqname] = s_aa_freq.values
    

# This code computes statistics for the amino acid counts and frequencies
# And then appends them to the end of the data frame.

df_stats_mean = df.mean(axis = 0, numeric_only = True)
df_stats_median = df.median(axis = 0, numeric_only = True)
df_stats_variance = df.var(axis = 0, numeric_only = True)
df_stats_std = df.std(axis = 0, numeric_only = True)

average_list = ['average']
df.loc['average'] = average_list + list(df_stats_mean)

median_list = ['median']
df.loc['median'] = median_list + list(df_stats_median)

variance_list = ['variance']
df.loc['variance'] = variance_list + list(df_stats_variance)

std_list = ['std dev']
df.loc['std dev'] = std_list + list(df_stats_std)

print(df)
df.to_csv(output_file_name)
