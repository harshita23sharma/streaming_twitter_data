import csv
import nltk
import re
with open('edit.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		#text = word_tokenize(row)
		kv=nltk.pos_tag(row)
		
		for k,v in kv:
			if re.match('^VB',v):
					print kv
					print k
					with open("newfile.txt", "a") as myfile:
						myfile.write(k)
						myfile.write("\n")
					myfile.close()
