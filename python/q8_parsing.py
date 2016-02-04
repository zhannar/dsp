# -*- coding: utf-8 -*-
"""Line above added to get rid of this error:
SyntaxError: Non-ASCII character '\xe2' in file q8_parsing.py on line 4, 
but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details

Per: http://stackoverflow.com/questions/21639275/python-syntaxerror-non-ascii-character-xe2-in-file

The football.csv file contains the results from the English Premier League. 
The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
goals scored for and against each team in that season (so Arsenal scored 79 goals 
against opponents, and had 36 goals scored against them). 

Write a program to read the file, then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.
"""

data = "football.csv"

import pandas as pd

# Step 1: Bring the data in.
football_df = pd.read_csv(data)

# Step 2: Create a new column which calclates the difference between goals and goals allowed.
football_df["Goals Difference"] = abs(football_df["Goals"] - football_df["Goals Allowed"])

# Step 3: Identify the minimum difference and pop out the information for it
# Reference: http://stackoverflow.com/questions/15741759/find-maximum-value-of-a-column-and-return-the-corresponding-row-values-using-pan
# This method gives all the information:
#print football_df.loc[football_df['Goals Difference'].idxmin()]

# This method pulls only the team name:
print football_df.loc[football_df['Goals Difference'].idxmin()]["Team"]










