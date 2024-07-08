# Allyn J. Schoeffler, PhD
# Loyola University New Orleans
# For usage and license, see MIT license

######
#package imports; do not edit
import pandas
import matplotlib.pyplot
import numpy
import scipy.stats

## Edit the df definition below to input your stats files.
## These files MUST be the direct, unedited output from 
## the counter_catalog.py script. 
## Edit the myoutputfile field to your esired output file name

# read the csv files from counter_catalog.py;
# edit to reflect your data.
df1 = pandas.read_csv('my_set1_output.csv')
df2 = pandas.read_csv('my_set2_output.csv')

# Edit the file name below to your desired file name
myoutputfile = 'my_sigstats.csv'

#### Do not edit anything below this line unless you are an experienced python user #####

# truncate the statsitics off the dataframe and re-store it
def cut_last_rows(dataframe, number_of_rows):
	count = 0
	while count < number_of_rows:
		dataframe = dataframe.drop(dataframe.index[-1])
		count = count + 1
	return dataframe

df1trunc = cut_last_rows(df1, 4)
df2trunc = cut_last_rows(df2, 4)

# This function performs a t-test given a set of two columns.
# It extracts the t-values and P-values from the output and returns them as a list.

def ttest_and_extract(set1, set2):
    TandP = scipy.stats.ttest_ind(set1, set2)
    #split1 = TandP.split('(').rstrip(')')
    #split2 = split1[1].split(',')
    #tlist = split2[0].split('=')
    #tvalue = tlist[1]
    #plist = split2[1].split('=')
    #pvalue = plist[1]
    tvalue = TandP[0]
    pvalue = TandP[1]
    return [tvalue, pvalue]

#These lines create a list of column headers and remove the first two column headers from the list
column_headers = df1.columns.tolist()
column_headers.pop(0)
column_headers.pop(0)

# Create an empty data frame to store the stats.
# Below, we create a dataframe in which the index is the statistic  

list_of_stats = ['t-value 1vs2', 'P-value 1vs2']

df = pandas.DataFrame(index = list_of_stats)

stat_list = []
for header in column_headers:
    aai_stat_list = ttest_and_extract(df1trunc[header], df2trunc[header])
    df[header] = aai_stat_list

print(df)
df.to_csv(myoutputfile)
