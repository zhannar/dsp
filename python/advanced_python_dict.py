# Part III - Dictionary

data = "python/faculty.csv"

# Import data
import pandas as pd

faculty_df = pd.read_csv(data)
df = pd.read_csv(data)


# Create some helper functions which will be used later...

def degree_parser(degrees):
    degrees = degrees.replace("Ph.D ", "Ph.D. ")
    degrees = degrees.replace("Ph.D.", "Ph.D.")
    degrees = degrees.replace("PhD", "Ph.D.")
    degrees = degrees.replace("ScD", "Sc.D.")
    degrees = degrees.replace("MS", "M.S.")
    degrees = degrees.replace("0", "")
    return degrees


def title_parser(title):
    title = title.replace("of Biostatistics", "")
    title = title.replace("is Biostatistics", "")
    title = title.rstrip()
    return title


"""
# ----------------------------------------------------------------------
# Q6. Create a dictionary in the below format:

# faculty_dict = { 'Ellenberg': [\
#               ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
#               ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
#                             ],
#               'Li': [\
#               ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
#               ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
#               ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
#                             ]
#             }
# ----------------------------------------------------------------------
"""

# Create empty dictionary to contain info:
faculty_dict = {}

# Reference:
# http://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe

for index, row in faculty_df.iterrows():
    # Part 1 - Extract out the name
    full_name = row['name']
    name_parts = full_name.split()
    last_name = name_parts[-1]

    # Part 2 - Extract and parse the degrees
    degrees = degree_parser(row[' degree'])

    # Part 3 - Extract and parse the title
    title = title_parser(row[' title'])

    # Part 4 - Combine them together into a list (along with email)
    teacher_info_list = [degrees, title, row[' email']]

    # Part 5 - Check if that last name is in the fictionary already.
    # If not, add them to a dictionary.
    # If yes, append it.
    if last_name not in faculty_dict:
        faculty_dict[last_name] = teacher_info_list
    else:
        faculty_dict[last_name] = [faculty_dict[last_name], teacher_info_list]

    # References:
# As dictionaries don't have a defined order, this provides a way to extract
# subsets of dictionaries.
# http://stackoverflow.com/questions/4194365/python-how-to-get-a-subset-of-dict/4194402#4194402

def get_range(dictionary, begin, end):
	import itertools
	print dict(itertools.islice(dictionary.iteritems(), begin, end))


get_range(faculty_dict, 0, 3)

"""
# ----------------------------------------------------------------------
# Q7. The previous dictionary does not have the best design for keys. 
# Create a new dictionary with keys as:

# professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
#                ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
#                ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
#                ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
#                ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
#            }
# ----------------------------------------------------------------------
"""
# Create empty dictionary to contain info:
professor_dict = {}

# Reference:
# http://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe

for index, row in faculty_df.iterrows():
    # Part 1 - Extract out the name
    full_name = row['name']
    name_parts = full_name.split()
    first_name = name_parts[0]
    last_name = name_parts[-1]
    name_tuple = (first_name, last_name)

    # Part 2 - Extract and parse the degrees
    degrees = degree_parser(row[' degree'])

    # Part 3 - Extract and parse the title
    title = title_parser(row[' title'])

    # Part 4 - Combine them together into a list (along with email)
    teacher_info_list = [degrees, title, row[' email']]

    # Part 5 - Add them to a dictionary
    professor_dict[name_tuple] = teacher_info_list



def print_sorted_dictionary(dictionary,key_sort_index,n):
	"""This function takes as an input a dictionary, an index of which element in the dictionary's
	key the user would like to sort by, and how many elements of the head of the sorted dictionary they want printed.
	Note: the key_sort_index is to enable tuple elements as keys. For example, if the dictionary looks is of the form:
	(a,b,c,d,e) and you wanted the dictionary sorted by column d, you would enter 3 (python is indexed to 0). If you
	want it sorted by c, you would enter 2."""

	original_keys = dictionary.keys()

	sorted_keys = sorted(original_keys, key = lambda person:person[key_sort_index])

	for key in sorted_keys[0:n]:
		print key, dictionary[key]

print_sorted_dictionary(professor_dict,0,3)

"""
# ----------------------------------------------------------------------
# Q8. It looks like the current dictionary is printing by first name. 
# Sort by last name and print the first 3 key and value pairs.

# ----------------------------------------------------------------------
"""

print_sorted_dictionary(professor_dict,1,3)