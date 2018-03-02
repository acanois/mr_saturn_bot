import nltk
from collections import Counter

saturn_file = open("mr-saturn-dialog.txt").read()
# because mr saturn randomly capitalizes, capitalized words get NNP'd, so... lower()
tokens = nltk.word_tokenize(saturn_file.lower()) 
tagged = nltk.pos_tag(tokens)

print(tokens)

tagtypes = []

# Sort everything by tag
def sort_tagtype():
	for i in range(len(tagged)):
		word = tagged[i][0]
		tagtype = tagged[i][1]
		if_tag_in_list(word, tagtype)

# Figure out if the type already in the list, and, if it is, write it to its own file
def if_tag_in_list(word, tagtype):
	if tagtype in tagtypes:
		file = open(tagtype + ".txt", "a")
		file.write('"%s", '  % word)
		file.close()
	else:
		file = open(tagtype + ".txt", "a")
		tagtypes.append(tagtype)
		file.write('"%s", ' % word)
		file.close()

sort_tagtype()