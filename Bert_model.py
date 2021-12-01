# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:23:52 2021

@author: Home
"""

#Installing the libraries
!pip install git+https://github.com/huggingface/transformers
!pip install tokenizers

from tokenizers.implementations import ByteLevelBPETokenizer

# Loading the created Tokenizer
tokenizer = ByteLevelBPETokenizer(
    "gdrive/MyDrive/dM1/vocab.json",
    "gdrive/MyDrive/dM1/merges.txt",
)

#Defining the model configuration
from transformers import RobertaConfig
config = RobertaConfig(
    vocab_size=52_000,
    max_position_embeddings=514,
    num_attention_heads=12,
    num_hidden_layers=6,
    type_vocab_size=1
)

#Reloading the tokenizer and initializing the model
from transformers import LineByLineTextDataset
from transformers import RobertaTokenizerFast

tokenizer = RobertaTokenizerFast.from_pretrained("gdrive/MyDrive/dM1", max_len=512)

from transformers import RobertaForMaskedLM
model = RobertaForMaskedLM(config=config)

#Building the dataset
dataset = LineByLineTextDataset(
    tokenizer = tokenizer,
    file_path ='gdrive/MyDrive/Train/2.txt', 
    block_size=128,
)
#Data collator
from transformers import DataCollatorForLanguageModeling 
data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=True, mlm_probability=0.15)

#Initializing the trainer
from transformers import Trainer, TrainingArguments
training_args = TrainingArguments(output_dir='gdrive/MyDrive/dM1', overwrite_output_dir=True,
                                  num_train_epochs=3,
                                  per_device_train_batch_size=32,
                                  save_steps=10_000,
                                  save_total_limit=2,
                                  
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
) 

#Training and saving the model
trainer.train()
trainer.save_model('gdrive/MyDrive/dM1')

#Language modelling
from transformers import pipeline

fill_mask=pipeline(
    'fill-mask',
    model='gdrive/MyDrive/M1',
    tokenizer='gdrive/MyDrive/M1'
)

fill_mask('<mask> ඉගෙනීමට ගියා')
