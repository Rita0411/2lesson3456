#!/usr/bin/python3
import string
f = open('/usr/share/licenses/python/LICENSE', 'r')
text = f.read()
f.close
text = text.lower()
for char in string.punctuation:
	text = text.replace(char, ' ')
words = text.split()
counts = {}
for word in words:
	if word in counts:
		counts[word] = counts[word] + 1
	else:
		counts[word] = 1
topw = ["", "", "", "", "","", "", "", "", ""]
topc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(10):
	maxw = " "
	maxc = 0
	for word in counts:
		if counts[word] > maxc:
			maxc = counts[word]
			maxw = word
	topw[i] = maxw
	topc[i] = maxc
	del counts[maxw]
for i in range(10):
	print(topw[i], '-', topc[i])


