#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 03:32:21 2018

@author: sunitapattanayak
"""

import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'EvcNB4LmlX9oa2Ph7ZVlzzlTv'
consumer_secret = 'CodhFzrVcBUhACk4Mkf5aUq3N8cGRhBLsWj4ib1E2KZvcL5SK1'
access_token = '961110803847045120-wxobmdtO7lMtfUrQzmH5LLmALX8hHbI'
access_secret = 'n4c5LQADnLg0B4FXsnEbRyyCpbk53joHINzg4XkvxOeWl'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

query = 'H1B'
max_tweets = 1000
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

with open('resu_2.txt', "w") as outfile:
    for entries in searched_tweets:
        outfile.write(str(entries))
        outfile.write("\n")

import json

with open('resu1_2.txt', "w") as outfile:
    for entries in searched_tweets:
        json_str=(json.dumps(entries._json))
        all_data = json.loads(json_str)       
        tweet = all_data["text"]  
        outfile.write(str(tweet))
        outfile.write("\n")
        
import requests
r = requests.get("http://api.nytimes.com/svc/search/v2/articlesearch.json?q=H1B&api-key=d40490ff6c8749778aa85d6a3535f6b8")
data = r.json()
len(data["response"]["docs"])

from bs4 import BeautifulSoup
news=[]
for i in data['response']['docs']:
    url = i['web_url']
    r = requests.get(url).text
    soup = BeautifulSoup(r,'html.parser')

    title = soup.title
    article_paragraphs = soup.find_all('p')
    article = ""
    for p in article_paragraphs:
        article=article+p.get_text()
        
    news.append(article)
len(news)

with open('resu4_2.txt', "w") as ou:
    for entries in news:
        ou.write(entries)
        ou.write("\n")
        
import requests
r = requests.get("http://api.nytimes.com/svc/search/v2/articlesearch.json?q=H1B&api-key=846f81f7cc4143d5bdc3b45fb3142b9c&begin_date=20110102&end_date=20111202")
data = r.json()
len(data["response"]["docs"])

from bs4 import BeautifulSoup
news1=[]
for i in data['response']['docs']:
    url = i['web_url']
    r = requests.get(url).text
    soup = BeautifulSoup(r,'html.parser')

    title = soup.title
    article_paragraphs = soup.find_all('p')
    article = ""
    for p in article_paragraphs:
        article=article+p.get_text()

    news1.append(article)
len(news1)

with open('resu4_1.txt', "w") as ou:
    for entries in news1:
        ou.write(entries)
        ou.write("\n")