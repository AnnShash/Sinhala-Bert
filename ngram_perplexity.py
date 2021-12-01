# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:21:08 2021

@author: Home
"""

# CMU toolkit should be downloaded using http://www.speech.cs.cmu.edu/SLM/toolkit_documentation.html
# Creating the vocab
!cat Train.txt | text2wfreq | wfreq2vocab -top 20000 > Train.vocab

# Building the model
!cat Train.txt | text2idngram -n 2 -vocab Train.vocab -buffer 100 -temp /tmp | \
   idngram2lm -idngram Train.id2gram -vocab Train.vocab -n 2 \
   -binary Train2gram.binlm -cutoffs 2 -witten_bell

# Computing the perplexity
!echo "perplexity -text Test.txt" | evallm -binary Train.2gram.binlm
