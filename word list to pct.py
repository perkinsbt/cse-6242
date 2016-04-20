# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 14:41:27 2016

@author: Perk
"""
import json
import requests
import csv
from tqdm import tqdm
from itertools import izip_longest

with open('sunlight API.txt','r') as api_file:
    api_key = api_file.read()
phrase_url='http://capitolwords.org/api/1/phrases/party.json'
phrase_param = {'apikey':api_key,'mincount':300}
with open('top_article_phrases.json') as phrases_json:
    phrase_dict = json.load(phrases_json)
phrase_set = set()
for lst in phrase_dict.values():
    for phrase in lst:
        phrase_set.add(phrase)
phrase_partisanship = {}
for wrd in tqdm(phrase_set,desc='Querying phrases...'):
    phrase_param['phrase'] = wrd
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
    else:
        phrase_partisanship[wrd] = rep/(rep+dem)
for k,v in tqdm(phrase_dict.iteritems(),desc='Writing word partisanship'):
    word_partisanship = []
    for word in v:
        for key,val in phrase_partisanship.iteritems():
            if key == word:
                word_partisanship.append((word,val))
    phrase_dict[k] = word_partisanship
with open('word_partisanship.csv','w') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(phrase_dict.keys())
    csv_out.writerows(izip_longest(*phrase_dict.values()))