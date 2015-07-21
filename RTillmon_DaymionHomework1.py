#!/usr/bin/env python

import re
with open('lyrics.txt') as f:
    new = " ".join(line.strip() for line in f)
    new = new.lower()
    nulist = list(new)
    wordList = re.sub("[^\w]", " ",  new).split()
    wordList.sort(key = lambda s: len(s))
print "\n By Length: "
for le in wordList:
    print le
print "\n Words in Alphabetical: "
wordList2 = re.sub("[^\w]", " ",  new).split()
wordList2.sort()
for i in wordList2:
    print i
print "\n Letters in Alphabetical: "
nulist.sort()
for ltrs in nulist:
    str(ltrs).replace(' ', '')
    print ltrs
print "\n Capitalize Each Word: "
print new.title()