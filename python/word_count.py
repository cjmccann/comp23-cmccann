import sys

try:
	fileName = sys.argv[1]
	f = open(fileName)
	d = {}

	for word in f.read().split():

		lowWord = word.lower()
		if lowWord in d:
			d[lowWord] += 1
		else:
			d[lowWord] = 1

	wordSum = 0
	
	for key in sorted(d.iterkeys()):
		wordSum += d[key]
		print "%s %s" % (key, d[key])

	print "There are %s words in this file." % (wordSum)

	f.close()
except:
	print "Error in opening file. Try again."
