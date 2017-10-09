#!/usr/bin/env python

from StudyAssistan import definitions as df
from sys import argv
import random as rd
import itertools as its

myfile = argv[1]
num = int(argv[2])
mydic = df.impdoc(myfile)
mywords = [x for x in mydic.keys()]

words = []
for x in range(num):
    word = rd.choice(mywords)
    words.append(word)
    mywords.remove(word)

for x in words: print(x)

print()

for word in words:
    df.choice(mydic, word)
