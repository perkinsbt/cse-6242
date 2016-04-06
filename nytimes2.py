# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 20:05:40 2016

@author: katherinemckenna
"""

from nytimesarticle import articleAPI
import csv
import os
key_word="Obamacare"

os.chdir('/Users/katherinemckenna/Documents/CSE6242/Project/Articles Pulling')
api = articleAPI('0358c9b864c6cad5603a6a32420c60be:7:74784865')


def parse_articles(articles):
    news = []
    for i in articles['response']['docs']:
        dic = {}
        #dic['id'] = i['_id']
        dic['desk'+"_"+key_word] = i['news_desk']
        dic['date'+"_"+key_word] = i['pub_date'][0:10] # cutting time of day.
        dic['section'+"_"+key_word] = i['section_name']
        #dic['type'] = i['type_of_material']
        dic['url'+"_"+key_word] = i['web_url']
        #dic['word_count'] = i['word_count']
        news.append(dic)
    return(news) 

def get_articles(date,query):
    all_articles = []
    for i in range(0,100): #NYT limits pager to first 100 pages. But rarely will you find over 100 pages of results anyway.
        try:
            articles = api.search(q = query,
               fq = {'source':["The New York Times"],'news_desk':['Business','National','Politics','Washington','Business Day']},
               begin_date = date + '0101',
               end_date = date + '1231',
               sort='oldest',
               page = str(i))
            articles = parse_articles(articles)
            all_articles = all_articles + articles
        except ValueError:
            print "No articles for this page"
    return(all_articles)


all_articles = []
for i in range(2015,2016):
    print 'Processing' + str(i) + '...'
    year =  get_articles(str(i),key_word)
    all_articles = all_articles + year

keys = all_articles[0].keys()


csv_file=key_word+".csv"
with open(csv_file, 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_articles)
    
