import os

from collections import Counter

f = open("checktex.txt", "r")

read_text = f.read()

res = Counter(read_text)

print(str(res))