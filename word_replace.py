import re
import pprint

with open("./cnn_news.txt","r") as f:
    data = f.read()

blank_txt = re.sub(r"[^a-zA-Z\n\t\r\f\v]"," ",data)

print(blank_txt)
