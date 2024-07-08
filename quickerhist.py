## Allyn J. Schoeffler, PhD
## and Elena Voisin
## Loyola University New Orleans
## MIT license
## Contact ajschoef@loyno.edu with questions.

###
# This script will take amino acid frequency .csv files
# as output by counter_catalog.py only
# and create histograms and boxen plots of those frequencies.
# The script assumes that you have three subsets:
# Psychrophiles, Mesophiles, and Thermophiles.
# (But, you can edit your labels.)
# It uses an accessible color scheme developed by Paul Tol and curated by David Nichols.
# (for more information, see https://davidmathlogic.com/colorblind/#%23D81B60-%231E88E5-%23FFC107-%23004D40)
# You must edit the names below to match the names of the .csv files output by counter_catalog.py,
# and make sure your files are in the same folder as this script.
# You must also be sure that the box.mplstyle file is in the same folder as this script. 

## package imports; do not edit
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import seaborn as sns
import scipy
import pandas as pd


# Edit the file names below to match the correct counter_catalog.py output files you created.
## Make sure the files have not been edited in any way after being created by the counter_catalog.py script!

psychro_df = pd.read_csv("psychro_output.csv")
meso_df = pd.read_csv("meso_output.csv")
thermo_df = pd.read_csv("thermo_output.csv")

# Edit the username field below to a label you want for your output files
username = 'my_protein'

# Edit the names below to reflect the three sets of counter_catalog .csv files you input above. 
# These labels will show up in legends on the output histograms.

userset1 = 'psychro'
userset2 = 'meso'
userset3 = 'thermo'


#####
#Don't edit anything below this line unless you are an experienced python coder ####

## Do not edit
# The following lists provide amino acid names, three-letter codes, and one-letter codes.
roinames = ['Alanine', 'Arginine','Asparagine', 'Aspartate', 'Cysteine', 'Glutamate', 'Glutamine', 'Glycine', 'Histidine', 'Isoleucine', 'Leucine', 'Lysine', 'Methionine', 'Phenylalanine', 'Proline', 'Serine', 'Threonine', 'Tryptophan', 'Tyrosine', 'Valine']
roi3names = ['ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLU', 'GLN', 'GLY', 'HIS', 'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL']
roiletters = ['A','R','N','D','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V']
numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

# To drop the last four rows of the column containing the mean, median, variance, and st.dev
psychro_dataset = psychro_df[:-4]
meso_dataset = meso_df[:-4]
thermo_dataset = thermo_df[:-4]

## Set the plot size for histograms and boxenplots
matplotlib.pyplot.rcParams["figure.figsize"] = (20,15)

## Set the plot style
matplotlib.pyplot.style.use('./box.mplstyle')

## The code below creates lists of values from the columns of interest

for n in numbers:
	roi = roinames[n]
	roi3 = roi3names[n]
	column_name = roiletters[n] + ' frequency'
	print(column_name)
	
	psychroset =list(psychro_dataset[column_name])
	print("Psychrophile values")
	print(psychroset)

	mesoset =list(meso_dataset[column_name])
	print("Mesophile values")
	print(mesoset)

	thermoset = list(thermo_dataset[column_name])
	print("Thermophile values")
	print(thermoset)

# These are the Schoeffler Lab color codes for various partitions.
# These come from an accessible color scheme designed by Paul Tol.
# For more information, see https://davidmathlogic.com/colorblind/#%23D81B60-%231E88E5-%23FFC107-%23004D40
	psychro_color = '#88CCEE'
	thermo_color = '#CC6677'
	meso_color = '#DDCC77'
	halo_color = '#44AA99'
	nonhalo_color = '#DDCC77'


# histogram for psychro, meso, thermo; with normalization
	plt.hist([psychroset, mesoset, thermoset], label = [userset1, userset2, userset3], color = [psychro_color, meso_color, thermo_color], density = True)
	plt.xlabel("Frequency of %ss" % roi)
	plt.ylabel("Normalized count")
	plt.title("%s Frequency (%s, %s, %s; normalized)" % (roi, userset1, userset2, userset3))
	plt.legend(fontsize = 20)
	plt.savefig("%s_%s_hist.png" % (username, roi3))
	plt.clf()


#specify the Tol palette for temperature niches
	TolSky = matplotlib.colors.hex2color('#88CCEE')
	TolGold = matplotlib.colors.hex2color('#DDCC77')
	TolRose = matplotlib.colors.hex2color('#CC6677')
	tol_palette_temp = sns.color_palette([TolSky, TolGold, TolRose])
	sns.set_palette(tol_palette_temp)

	sns.boxenplot(data = [psychroset, mesoset, thermoset])
	plt.ylabel("Frequency of %ss" % roi)
	plt.title("%s Frequency (%s, %s, %s)" % (roi, userset1, userset2, userset3))
	plt.xticks([], labels = '')
	plt.savefig("%s_%s_temp_box.png" % (username, roi3))
	plt.clf()

