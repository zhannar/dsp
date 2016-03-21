def has_no_e(string):
	if string.find("e") == -1:
		return True
	else:
		return False

fin = open("words.txt")

total_words = 0
no_e_words = 0

for line in fin:
	line = line.strip()
	total_words += 1

	if has_no_e(line):
		no_e_words += 1
		print line


total_words = float(total_words)

print "Percentage of Words w/o an E:", no_e_words / total_words
