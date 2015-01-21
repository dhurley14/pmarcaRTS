import re
import os
import sys
import json
import nltk

STOP_WORDS = nltk.corpus.stopwords.words('english')
CORPUS_FILE = open("corpus.txt", "w")

articleTexts = json.loads(open("DevinResults.json").read())

for someText in articleTexts:
    html = someText.get("text","")
    words = html.split()
    words = [x.lower() for x in words if re.match('^[\w-]+$', x) is not None] # take only alphanumerics
    words = [word.lower() for word in words]
    words = [word for word in words if word not in STOP_WORDS]

    CORPUS_FILE.write(" ".join(words) + "\n")

CORPUS_FILE.close()
