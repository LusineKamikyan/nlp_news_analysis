#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:51:07 2020

@author: Lusine Kamikyan
"""

from nltk import word_tokenize, pos_tag
from collections import Counter


# number of nouns
def nouns(article):
    ''' string --> int
    Given a string of text, tokenize the text and pull out only the nouns.'''
    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = word_tokenize(article)
    all_nouns = [word for (word, pos) in pos_tag(tokenized) if is_noun(pos)] 
    num_nouns = len(all_nouns)
    return num_nouns

# number of adjectives
def adjective(article):
    ''' string --> int
    Given a string of text, tokenize the text and pull out only the adjectives.'''
    is_adj = lambda pos: pos[:2] == 'JJ'
    tokenized = word_tokenize(article)
    all_adj = [word for (word, pos) in pos_tag(tokenized) if is_adj(pos)] 
    num_adj = len(all_adj)
    return num_adj

# number of unique words
def unique_words(article):
    ''' string --> int
    This function calculates the number of unique words
    in the article'''
    tokenized = word_tokenize(article)
    num_unique_words = len(Counter(tokenized).keys())
    return num_unique_words

# number of total words
def total_words(article):
    ''' string --> int
    This function calculates the number of total words
    in the article'''
    tokenized = word_tokenize(article)
    num_total_words = sum(Counter(tokenized).values())
    return num_total_words    


