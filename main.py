# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 21:24:41 2019

@author: Fenix
"""
from flask import Flask, jsonify,request
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import tweepy


auth = tweepy.OAuthHandler('hbakqhcJ915mtMvQKP23herbf', 'dg5VtGLjfS21SsgyleD5Oms1YnI8prGD4AN49XCxjcnDCfMawc')
auth.set_access_token('1487072078-7WkhXqjR8GkMnajbmt5SCPasZhx3CXlGGfmTHm1', '3qirENXKlzaaNFAEQxtO3bBXQxaonzHJc5tprvYzl2iKE')

api = tweepy.API(auth)

def tweet_formatter(tweet):
    return '<div style="max-width:600px;padding:20px;border-radius:20px;border: 2px solid blue">' + tweet + '</div><br/><br/><br/>'
    
def word_cloud_func(tweets):
    
    val = ''
    comment_words = ' '
    stopwords = set(STOPWORDS) 
    
    val = str(tweets) 
    print(val)
    # split the value 
    tokens = val.split() 
      
    # Converts each token into lowercase 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower() 
          
    for words in tokens: 
        comment_words = comment_words + words + ' '
  
      
    wordcloud = WordCloud(width = 800, height = 800, 
                    background_color ='white', 
                    stopwords = stopwords, 
                    min_font_size = 10).generate(comment_words) 
      
    # plot the WordCloud image                        
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
      
    plt.show() 
    
    return wordcloud


app = Flask(__name__)
    
@app.route('/',methods=['GET','POST'])
def home():
    public_tweets = api.home_timeline()
    str='<div style="align: left"><h1 style="text-align:center">Trending Tweets</h1><br/><br/>'
    word_cloud = ''
    word_cloud_str = ''
    for tweet in public_tweets:
        str += tweet_formatter(tweet.text)
        word_cloud_str += tweet.text
        
    word_cloud = word_cloud_func(word_cloud_str)
    print(word_cloud)
    str+= '</div>'
    
    #trending = api.trends_place({id: '10'})
    #print(trending)   
    
    
    return str

app.run(port=5555)