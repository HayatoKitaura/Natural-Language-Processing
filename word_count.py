from collections import Counter
import pprint

with open("./cnn_news.txt", "r") as f:
    data = f.read()

c = Counter(data)
pprint.pprint(c.most_common())
