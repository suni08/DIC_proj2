#!/usr/bin/python
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

List = open("output.txt").readlines()

import collections

counter = collections.Counter()

for line in List:
    k,v=line.strip().split("\t",2)
    counter[k]+=int(v)
Most = counter.most_common(10)
words=[]
for line in Most:
	words.append(line[0])

stop_words = list(stopwords.words('english'))
punc = [',',';','""',"''", "'", '"', ':',  '.', '-']
punc2 = ["'s", "'re", ")","(", "@", "?","'ve", "...", "`","``","@", "got", "please", "n't", "even"]
all_stop_words = sum([stop_words, punc, punc2], [])
# input comes from STDIN (standard input)

for line in sys.stdin:
	for w in range(len(words)):
		for w2 in range(w,len(words)):
			if(words[w]!=words[w2] and (words[w] in line) and (words[w2] in line)):
    				if unicode(words[w].lower(),"utf-8") not in all_stop_words and unicode(words[w2].lower(),"utf-8") not in all_stop_words:
        				print '%s-%s\t%s' % (words[w].lower(),words[w2].lower(),1)
        





			
				
