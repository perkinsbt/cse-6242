# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 09:46:30 2016

@author: Perk
"""

import requests
from progressbar import ProgressBar
with open('sunlight API.txt','r') as api_file:
    api_key = api_file.read()
date_lst = []
for year in range(2000,2017):
    for month in range(1,11):
        date_lst.append('{}0{}'.format(year,month))
    for month in range(11,13):
        date_lst.append('{}{}'.format(year,month))
req_url='http://capitolwords.org/api/1/phrases.json'
req_param = {'apikey':api_key,'entity_type':'month',
                 'sort':'count desc'}
phrase_set = set()
req_bar = ProgressBar()
for n in req_bar(range(1,6)):
    req_param['n'] = n
    for j in range(1,6):
        req_param['page'] = j
        for mon in date_lst:
            req_param['entity_value'] = mon
            phrase_req = requests.get(req_url,params=req_param)
            phrase_req.raise_for_status()
            req_json = phrase_req.json()
            for line in req_json:
                phrase_set.add(line['ngram'])
print len(phrase_set)
with open('total_phrases.txt','w') as phrases:
    phrases.write('\n'.join(phrase_set))