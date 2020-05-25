#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:53:06 2020

@author: Lusi e Kamikyan
"""

import pandas as pd

import nltk.corpus 
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer 
from nltk.sentiment import vader
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from textblob import TextBlob


# stemming
def stem_articles(article):
    ''' string --> string
    This function stems the words'''
    porter_stemmer = PorterStemmer()
    tokens = article.split()
    stemmed_tokens = [porter_stemmer.stem(token) for token in tokens]
    return ' '.join(stemmed_tokens)


# lemmatize
def lemmatize_articles(article):  
    ''' string --> string
    This function lemmatizes the article words'''
    lemmatizer = WordNetLemmatizer()
    w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
    lemm_list_word = [lemmatizer.lemmatize(w) for w in w_tokenizer.tokenize(article)]
    return ' '.join(lemm_list_word)

# sentiment analysis
def sentiment_scores(df):
    ''' pandas df --> (pandas df, pandas df)
    This function gets the sentiment scores 
    (polarity and subjectivity) for each article'''
    #using polarity of vader
    pol = lambda x: SentimentIntensityAnalyzer().polarity_scores(x)
    # using subjectivity of textblob
    sub = lambda x: TextBlob(x).sentiment.subjectivity
    #pol = lambda x: TextBlob(x).sentiment.polarity 
    # create subjectivity df
    subjectivity_df = pd.DataFrame(columns = ['subjectivity'])
    subjectivity_df['subjectivity'] = df['cleaned_content'].apply(sub)
    # create polarity df
    polarity_df = pd.DataFrame(df['cleaned_content'].apply(pol))
    polarity_df = pd.DataFrame(list(polarity_df.cleaned_content), index = polarity_df.index)
    return subjectivity_df, polarity_df

# calculating topic modeling related matrices
def topic_modeling(df, stop_words, min_df, max_df):
    '''This function takes in a list of stop words, '''
    cv_tfidf_nmf = TfidfVectorizer(ngram_range=(1,2),stop_words = stop_words, min_df = 0.05, max_df = 0.9)
    news_article_tfidf_nmf = cv_tfidf_nmf.fit_transform(df.cleaned_content)

    news_article_tfidf_transpose_nmf = news_article_tfidf_nmf.transpose()

    nmf_model_tfidf = NMF(40)
    doc_topic = nmf_model_tfidf.fit_transform(news_article_tfidf_nmf)
    index_list = ["component_1","component_2", "component_3", "component_4",
              "component_5","component_6","component_7", "component_8", 
              "component_9","component_10","component_11","component_12",
              "component_13", "component_14","component_15","component_16",
              "component_17", "component_18", "component_19","component_20",
             "component_21","component_22", "component_23", "component_24",
              "component_25", "component_26","component_27", "component_28", 
              "component_29","component_30","component_31","component_32",
              "component_33", "component_34",
              "component_35", "component_36","component_37", "component_38", 
              "component_39","component_40"]
    topic_word = pd.DataFrame(nmf_model_tfidf.components_.round(3),
             index = index_list,
             columns = cv_tfidf_nmf.get_feature_names())
    return topic_word, nmf_model_tfidf, cv_tfidf_nmf, doc_topic


# display the topics of the articles
def display_topics(model, feature_names, no_top_words, topic_names=None):
    '''This function displays the topics of the articles'''
    for ix, topic in enumerate(model.components_):
        if not topic_names or not topic_names[ix]:
            print("\nTopic ", ix)
        else:
            print("\nTopic: '",topic_names[ix],"'")
        print(", ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))

