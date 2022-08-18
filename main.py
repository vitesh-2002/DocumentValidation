#NLTK library for natural language processing, tokenizing, tagging, and parsing text
import nltk
import string
text = 'Computers do not speak English. So you must learn languages like Java, Python, C, and others. Fascinating.'
from nltk.tokenize import sent_tokenize
sentences = sent_tokenize(text)
# print(sentences)
from nltk.tokenize import word_tokenize
words = word_tokenize(text)
# print(words)
# print(len(words))
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
words = [word for word in words if word not in stop_words]
# print('Without stopwords: ', words)
punctuations = list(string.punctuation)
words = [word for word in words if word not in punctuations]
# print('Without punctuation or stopwords: ', words)

import urllib.request
url = "https://www.gutenberg.org/files/1342/1342-0.txt"
text = urllib.request.urlopen(url).read().decode()
# print(text)

# Tokenize
from nltk.tokenize import word_tokenize
text = word_tokenize(text)

# Remove stopwords
from nltk.corpus import stopwords
stops = stopwords.words('english')
# print(stops)
words = [word for word in text if word not in stops]

# Remove punctuations
import string
punctuations = list(string.punctuation)
# print(punctuations)

words = [word for word in words if word not in punctuations]
# print("Without punctuations:", words)

# Bigrams
from nltk.metrics import BigramAssocMeasures
from nltk.collocations import BigramCollocationFinder
bigram_collocation = BigramCollocationFinder.from_words(words)
# Top 10 most occurring collocations
print("Bigrams:", bigram_collocation.nbest(BigramAssocMeasures.likelihood_ratio, 10))