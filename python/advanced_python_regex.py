# Step 0: Bring the data in.
data = "faculty.csv"
import pandas as pd
faculty_df = pd.read_csv(data)


# ----------------------------------------------------------------------
# Q1. Find how many different degrees there are, and their frequencies: 
# Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
# ----------------------------------------------------------------------


# Step 1 : Collapse multiple entries in a column to a string.
degree_string = str()

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

# ----------------------------------------------------------------------
# Q2. Find how many different titles there are, and their frequencies: 
# Ex: Assistant Professor, Professor
# ----------------------------------------------------------------------

# Method 1: Using pandas built in series method 'value_counts().' This is
# less favorable for the degrees question because while ppl generally have 
# only 1 title, they may and the dataset confirms not infrequently have 
# multiple degrees.

print faculty_df[" title"].value_counts()

# Method 2: Original Method, creating a dictionary of counts
# Step 1: Collapse multiple entries in a column to a list & clean up/remove extra info.

titles_list = []

for title in faculty_df[" title"]:
	title = title.replace("of Biostatistics", "")
	title = title.replace("is Biostatistics", "")
	titles_list.append(title.rstrip()) #rstrip removes any extra spaces hanging around...


# Step 2: Convert list into dicitonary of counts...
print dict_counts(titles_list)


# ----------------------------------------------------------------------
# Q3. Search for email addresses and put them in a list. 
# Print the list of email addresses.
# ----------------------------------------------------------------------

email_list = []
	
for email in faculty_df[" email"]:
	email_list.append(email.rstrip())

print email_list

# ----------------------------------------------------------------------
# Q4. Find how many different email domains there are (Ex: 
#	mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.). 
#	Print the list of unique email domains.
# ----------------------------------------------------------------------

email_domain_list = []

for email in email_list:
	######## Part 1: Extract the domain out of the email ######################

	# Method 1: This uses regex to capture everything which comes after the @
	#email_domain = re.findall('.*@([^ ]*)',email)
	#print email_domain

	# Method 2: This splits the email into two parts, everything to the left 
	# of the @ and everything to the right. The stuff to the right is the email domain
	z = email.split("@")
	email_domain = z[1]
	
	####### Part 2:  Check if the email_email has already been added to the domain list.
	# If it hasn't, add it. ############################################
	if email_domain in email_domain_list:
		continue
	else:
		email_domain_list.append(email_domain)

print email_domain_list