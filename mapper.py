#!/usr/bin/python
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
stop_words = list(stopwords.words('english'))
punc = [',',';','""',"''", "'", '"', ':',  '.', '-']
punc2 = ["'s", "'re","th",")","(", "@", "?","'ve", "...", "`","``","@", "got", "please", "n't", "even"]
all_stop_words = sum([stop_words, punc, punc2], [])
# input comes from STDIN (standard input)
x=""
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    for w in words:
	word=re.sub('[^a-zA-Z-]', '',w.lower())
	if(word != ""):
    		if unicode(word,"utf-8") not in all_stop_words and not w.isdigit():
        		print '%s\t%s' % (word ,1)

        
