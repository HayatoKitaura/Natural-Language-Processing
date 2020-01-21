from collections import Counter
import pprint

with open("../cnn_news.txt","r") as f:
    data = f.read()

words = data.split()
words_list = Counter(words)

pprint.pprint(words_list)

