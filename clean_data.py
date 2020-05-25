#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:48:23 2020

@author: Lusine Kamikyan
"""
import re
import string

def initial_clean_data(df):
    ''' pandas df --> pandas df
    
    This function cleans the dataframe by removing some of the 
    columns that won\'t be used in the analysis process,  
    removes the records that have empty or Null content'''
    # list of columns to be removed
    col_list = ['id','section', 'url','category', 'digital', 'author']
    # We will keep all the news publications
    # We will drop the columns 'section', 'url', 'category', 'digital', 'author'
    df = df.drop(col_list,axis = 1)
    # remove the records that are empty or Null
    df = df[df.content != '']
    df = df[df.content.notnull()]
    return df


def clean_articles_stage2(article):
    ''' string --> string
    This function removes the punctuations, 
    makes the letters lower case, 
    removes words containing numbers'''
    article = article.lower() # make the letters lower case
    article = re.sub('\[.—*?-\]', '', article) # remove punctuation
    article = re.sub('“','', article)
    article = re.sub('”','',article)
    article = re.sub('’','',article)
    article = re.sub('—','',article)
    article = re.sub('\n', '', article)
    article = re.sub('[%s]' % re.escape(string.punctuation), '',article) #replace punctuation with empty space
    article = re.sub('\w*\d\w', '', article) # remove words containg numbers
    article = re.sub('\w*\d', '', article)
    article = ' '.join(article.split()) # remove all extra spaces 
    return article

