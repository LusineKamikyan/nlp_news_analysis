#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 14:08:16 2020

@author: Lusine Kamikyan
"""


import sqlite3
import pandas as pd

def get_data_df(year):
    '''Int --> pandas dataframe
    
    This function accesses the database where 
    the data is stored and returns all the news
    records from the given year as a pandas dataframe
    '''
    # the file is in .db format
    # conecting to the sqlite db
    mypath =  '/Users/aminenhila/MyGithubRepo/nlp_news_analysis/Data/all-the-news.db'
    conn = sqlite3.connect(mypath)
    res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # get the table name
    for i in res:
        table_name = i[0]
        #print(table_name)
    # the table name is longform
    # get all the records from the table
    query = conn.execute("SELECT * FROM "+table_name)
    # get the column names
    cols = [column[0] for column in query.description]
    results= pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
    # In this project we will focus on year 2017
    return results[results.year == 2017]
        


