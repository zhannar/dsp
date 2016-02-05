
# Step 0: Bring the data in.
data = "faculty.csv"
import pandas as pd
faculty_df = pd.read_csv(data)

# Step 1 & 2 : Collapse multiple entries in a column to a string.
degree_string= str()

for set_of_degrees in faculty_df[" degree"]:
	degree_string += set_of_degrees + " " #The space is added as a precaution
	


# 2) Clean-Up -
# Note: 'replace' method only works on strings.

degree_string = degree_string.replace("Ph.D ", "Ph.D. ")
degree_string = degree_string.replace("Ph.D.", "Ph.D.")
degree_string = degree_string.replace("PhD", "Ph.D.")

degree_string = degree_string.replace("ScD", "Sc.D.")
degree_string = degree_string.replace("MS", "M.S.")
degree_string = degree_string.replace("0", "")

# Step 3 : Convert string into list via regex. This breaks up the string into "words"
# ... all continuous non-whitespace
import re
degrees_list = re.findall( "\S+", degree_string)

# Step 4 : Define & use a function to convert lists into dictionary counts

def dict_counts(list):
	"""Adapted from 'Python for Everybody' - Chapter on Dictionaries.
	Basically, this takes a list as an input, and outputs a dictionary of
	counts for each item in the list. 

	Note: this assumes the inputed list is itself clean to begin with...
	 
	Logic: When we encounter a new item, we need to add a new entry in the
	dictionary and if this the second or later time we have seen the item,
	we simply add one to the count in the dictionary under that item."""

	dictionary = {}

	for item in list:
		

		if item not in dictionary:
			dictionary[item] = 1
		else :
			dictionary[item] = dictionary[item] + 1

	return dictionary
	print dictionary

print dict_counts(degrees_list)

