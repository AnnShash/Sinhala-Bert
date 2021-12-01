# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:22:04 2021

@author: Home
"""

import nltk
import re
import matplotlib.pyplot as plt
import math 

f = open('DATA_FINAL.txt','r',encoding = 'utf-8')
content = f.read()
f.close()
tokens = nltk.word_tokenize(content)

# get only sinhala unicode charactors
regex = re.compile(u'[^\u0D80-\u0DFF]', re.UNICODE)
tokens = [regex.sub('', w) for w in tokens]

# Obtaining the frequency and sorting
frequency = {}
for word in tokens:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency = {key:value for key,value in frequency.items()}
frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True) 

# Printing the most frequent words in the dataset
top_10 = list(frequency)[1:11]
print(top_10)

# Plotting 
frq = [c for (w,c) in frequency][1:-1]
rank = list(range(1,len(frq)+1))
r = [math.log(x) for x in rank]
f = [math.log(x) for x in frq]
plt.plot(f,r)
plt.title("Zipf's Law Behavior")
plt.xlabel("log(rank)")
plt.ylabel("log(frequency)")
