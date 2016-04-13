# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 14:41:27 2016

@author: Perk
"""
import requests
import json
from progressbar import ProgressBar
pbar = ProgressBar()
with open('sunlight API.txt','r') as api_file:
    api_key = api_file.read()
dem_word_lst = []
rep_word_lst = []
phrase_url='http://capitolwords.org/api/1/phrases/party.json'
phrase_param = {'apikey':api_key,'mincount':700}
with open('total_phrases.txt') as phrases:
    phrase_set = phrases.read().split('\n')
for ngram in pbar(phrase_set):
    phrase_param['phrase'] = ngram
    ngram_req = requests.get(phrase_url,params=phrase_param)
    ngram_req.raise_for_status()
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
        continue
    elif rep/(rep+dem) > 0.70:
        rep_word_lst.append((ngram,rep/(rep+dem)))
    elif dem/(dem+rep) > 0.70:
        dem_word_lst.append((ngram,dem/(dem+rep)))
with open('rep_word_count.json','w') as rep_file:
    json.dump(rep_word_lst,rep_file)
with open('dem_word_count.json','w') as dem_file:
    json.dump(dem_word_lst,dem_file)