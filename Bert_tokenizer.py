# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:22:48 2021

@author: Home
"""

# Installing the libraries
!pip install git+https://github.com/huggingface/transformers
!pip install tokenizers

from tokenizers import ByteLevelBPETokenizer
# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer()

paths = ['gdrive/MyDrive/Train/Train.txt']

# Customize training
tokenizer.train(files=paths, vocab_size=52_000, min_frequency=2, 
                special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "[UNK]",
    "<mask>",
])

# Saving the tokenizer to the directory
tokenizer.save_model("gdrive/MyDrive")
