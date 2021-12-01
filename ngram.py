# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:17:58 2021

@author: Home
"""

import nltk, re, string, collections
from nltk.util import ngrams

def ngram(infile):
    """ This will find the most common uni, bi and tri gram in the dataset """
    f = open(infile,'r',  encoding = 'utf-8')
    data = f.read()
    f.close()
    tokens = nltk.word_tokenize(data) # Extract only the sinhala words
    regex = re.compile(u'[^\u0D80-\u0DFF]', re.UNICODE)
    tokens = [regex.sub('', w) for w in tokens]
    
    bi = ngrams(tokens, 2) # Bi gram          
    bi_freq = collections.Counter(bi)
    tri = ngrams(tokens, 3) # Tri gram
    tri_freq = collections.Counter(tri)
    
    print('Most common bigrams') # Top 10 bi grams 
    print(bi_freq.most_common(10))
    print('\n')
    print('Most common trigrams') # Top 10 tri grams
    print(tri_freq.most_common(10))
