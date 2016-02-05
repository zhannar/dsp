# ----------------------------------------------------------------------
# Part II - Write to CSV File
# Q5. Write email addresses from Part I to csv file.
# ----------------------------------------------------------------------

data = "faculty.csv"

# Import data
import pandas as pd
faculty_df = pd.read_csv(data)

# Create a list of the emails.
email_list = []
	
for email in faculty_df[" email"]:
	email_list.append(email.rstrip())

# Create & open a file for writing
csvfile = open("emails.csv","w")

# Write the file & close it.
for email in email_list:	
	csvfile.write(str(email))
	csvfile.write("\n")

csvfile.close()