# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 14:41:27 2016

@author: Perk
"""
import requests
import csv
from progressbar import ProgressBar
pbar = ProgressBar()
with open('sunlight API.txt','r') as api_file:
    api_key = api_file.read()
word_partisanship = []
phrase_url='http://capitolwords.org/api/1/phrases/party.json'
phrase_param = {'apikey':api_key,'mincount':300}
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
    else:
        word_partisanship.append((ngram,rep/(rep+dem)))
with open('word_partisanship.csv','w') as out:
	csv_out = csv.writer(out)
	for row in word_partisanship:
		csv_out.writerow(row)