fin = open("words.txt")

for line in fin:
	line = line.strip()
	if len(line)>= 15:
		print line

