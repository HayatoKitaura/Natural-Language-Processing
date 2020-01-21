import re
from collections import Counter
import pprint

with open("../cnn_news.txt","r") as f:
    data = f.read()

word = re.split('(..)',data)[1::2]
word_list = Counter(word)

pprint.pprint(word_list)
