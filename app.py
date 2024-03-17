#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from SentimentAnalysis import calculate_sentiment

st.title('Sentiment Analysis')

user_input = st.text_area("Enter text to analyze", "")

if st.button('Analyze'):
    result = calculate_sentiment(user_input)
    st.write('Sentiment score:', result)

