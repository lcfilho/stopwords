import nltk
import string
import sys
from nltk.corpus import stopwords

def stopword():
    with open(sys.argv[1],"r+") as f: 
        with open('s_stopwords.txt','w') as h:
            for line in f.readlines():
                print(" ".join([word for word in line.lower().translate(str.maketrans('', '', string.punctuation)).split() if len(word) >=4 and word not in stopwords.words('portuguese')]), file=h)

if __name__ == "__main__":
    stopword()


