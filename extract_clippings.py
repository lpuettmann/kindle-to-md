# -*- coding: utf-8 -*-

"""Transform Kindle clippings to Jekyll Markdown blog post"""

# Specify the title and author of the book
bookStr = "Moby Dick: or, the White Whale (Melville, Herman)"

assert(isinstance(bookStr, str)) # check if string
assert(len(bookStr) > 1)

f = open('My Clippings.txt', 'r')
fileCont = f.read()
exStr = fileCont
strList = exStr.splitlines()
nrLines = len(strList)

# Find beginning of clippings in the document
iDelStart = {}

for i in range(0, nrLines):
	strLine = strList[i]
	iDelStart[i] = strLine.find("==========")	

ixStart = [key for key, val in iDelStart.items() if val==0]

# Find clippings belonging to certain book
iBookStart = {}

for i in range(0, nrLines):
	strLine = strList[i]
	iBookStart[i] = strLine.find(bookStr)	

ixBook = [key for key, val in iBookStart.items() if val==0]

if not ixBook:
  print("No clippings for this book.")

else:
	# Form a title that can be displayed as URL
	saveStr = bookStr.lower()
	saveStr = saveStr.replace(' ', '-')
	saveStr = saveStr.replace('ä', 'ae')
	saveStr = saveStr.replace('ö', 'oe')
	saveStr = saveStr.replace('ü', 'ue')
	saveStr = saveStr.replace('ß', 'ss')

	# Delete special characters
	delStr = '(){}<>,:!?_*!$%/.#+'

	for s in saveStr:
		if s in delStr:
			saveStr = saveStr.replace(s, '')

	# Truncate
	maxLength = 50
	saveStr = saveStr[:maxLength] if len(saveStr) > maxLength else saveStr

	# Extract name of author and of title
	aStart = bookStr.rfind("(")
	assert(aStart != -1)
	aName = bookStr[aStart + 1 : -1] # author
	tName = bookStr[0:aStart] # title
	tName = tName.rstrip()
	assert(len(tName) > 1)

	# Write new blog post
	g = open(saveStr + '.md', 'w')
	g.write('---\n')
	g.write('layout: post\n')
	g.write('title: \'"' + tName + '"' + ", by " + aName + '\'\n')
	g.write('---\n')
	g.write('\n')

	# Write every clipping to file
	for i in range(0, len(ixBook)):
		ixLarger = [k for k in ixStart if k >= ixBook[i]]
		extrLine = min(ixLarger) - 1
		textSec = strList[extrLine]
		g.write('>')
		g.write(textSec)
		g.write('\n\n')

	g.close()
	print("Author: " + aName + "\nTitle: " + tName + "\nDone!")

f.close()
