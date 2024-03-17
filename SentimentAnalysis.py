#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import spacy


# In[8]:


# Create affin dataframe
afinn = pd.read_csv('Afinn.csv', sep=',', encoding='latin-1')

# Convert the affin dataframe to dictionary
affinity_scores = afinn.set_index('word')['value'].to_dict()


# In[9]:


nlp = spacy.load('en_core_web_sm')
sentiment_lexicon = affinity_scores

def calculate_sentiment(text: str = None):
    sent_score = 0
    if text:
        sentence = nlp(text)
        print(sentence)
        for word in sentence:
            print(word, sentiment_lexicon.get(word.lemma_, 0))
            sent_score += sentiment_lexicon.get(word.lemma_, 0)
    return sent_score

