'''
Exercise 1
Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and
converts them to lowercase.
Hint: The string module provides strings named whitespace, which contains space, tab, newline, etc., and punctuation
which contains the punctuation characters. Let’s see if we can make Python swear:

import string
print string.punctuation
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

'''
file = "/Users/Zhanna/Documents/Coding_Projects/ds/metis/prework/dsp/z_Other_Learning_code/ThinkPython/articles_confederation.txt"

fin = open(file)

text = fin.readlines()
print type(text)

print len(text)

words=[]
import string
punctuation = string.punctuation


for line in text:
    # Removes punctuation
    line = line.translate(None, punctuation)
    # Removes white spaces at ends
    line = line.strip()
    # Removes white spaces between lines
    words = words + line.split()
for i in range(len(words)):
    words[i] = words[i].lower()

print words

# Resources:
# Use of translate:
# http://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python
