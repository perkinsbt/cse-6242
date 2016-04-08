# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 09:46:30 2016

@author: Perk
"""

import requests
import json
with open('sunlight API.txt','r') as api_file:
    api_key = api_file.read()
date_lst = []
dem_word_lst = []
rep_word_lst = []
for year in range(2000,2017):
    for month in range(1,11):
        date_lst.append('{}0{}'.format(year,month))
    for month in range(11,13):
        date_lst.append('{}{}'.format(year,month))
req_url='http://capitolwords.org/api/1/phrases.json'
req_param = {'apikey':api_key,'entity_type':'month',
                 'sort':'tfidf desc','mincount':200}
phrase_url='http://capitolwords.org/api/1/phrases/party.json'
phrase_param = {'apikey':api_key,'mincount':200}
for n in range(1,6):
    req_param['n'] = n
    for mon in date_lst:
        req_param['entity_value'] = mon
        phrase_req = requests.get(req_url,params=req_param)
        req_json = phrase_req.json()
        phrase_lst = []
        for line in req_json:
            phrase_lst.append(line['ngram'])
        for ngram in phrase_lst:
            phrase_param['phrase'] = ngram
            ngram_req = requests.get(phrase_url,params=phrase_param)
            ngram_json = ngram_req.json()
            dem = 0.0
            rep = 0.0
            for line in ngram_json['results']:
                count = line['count']
                party = line['party']
                if party in ('R','Republican'):
                    rep += count
                elif party in ('D','Democrat'):
                    dem += count
            if (rep and dem) == 0.0:
                break
            elif rep/(rep+dem) > 0.80:
                rep_word_lst.append((ngram,rep/(rep+dem)))
            elif dem/(dem+rep) > 0.80:
                dem_word_lst.append((ngram,dem/(dem+rep)))
with open('rep_word_count.json','w') as rep_file:
    json.dump(rep_word_lst,rep_file)
with open('dem_word_count.json','w') as dem_file:
    json.dump(dem_word_lst,dem_file)