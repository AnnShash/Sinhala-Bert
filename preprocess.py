# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:17:04 2021

@author: Home
"""

import re
def preprocess(infile, outfile):
    """ This will preprocess the given text """
    reg1 = '[0-9]{4}.*?[0-9]{2}.*?[0-9]{2}.*?[0-9]{2}.*?[0-9]{2}.*?[0-9]{2}.*?'
    reg2 = re.compile(u'[^\u0D80-\u0DFF"num"]', re.UNICODE)
    
    f1 = open(infile, 'r', encoding = 'utf-8')
    txt = f1.read()
    txt = re.sub(reg1,'',txt)       # Removing date formats
    txt = re.sub('[A-Za-z]','',txt) # Removing English characters
    txt = re.sub('\d+','num', txt)  # Replacing digits
    sentences = txt.split('.')      # Spliting data to obtain sentences
    
    f2 = open(outfile, 'w', encoding = 'utf-8')
    for sentence in sentences:
        words = sentence.split()
        word = [reg2.sub('', w) for w in words] # Extracting Sinhala characters
        sentence = ' '.join(word)
        f2.write(sentence)
        f2.write('.\n')
    f2.close()
    f1.close()
