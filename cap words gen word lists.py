# -*- coding: utf-8 -*-
"""
This file will generate lists of the most commonly used words by Republicans
and Democrats.  You need a valid API key and to save the API key in the file
'sunlight API.txt' in the same directory as this .py file.
"""
import requests
import math
from collections import Counter
import numpy as np
#reads the API key
with open('sunlight API.txt','r') as api_file:
    api_key = api_file.read()
'''search parameters for finding the number of members of one party whose
terms began after 1996'''
def get_leg_ids(party):
    url='https://congress.api.sunlightfoundation.com/legislators'
    #query parameters to find out the number of records that exist
    bio_req = {'party':party,'fields':'count','all_legislators':'true',
               'term_start__gte':'1996-01-01','apikey':api_key}
    num_req = requests.get(url, params=bio_req)
    num_json = num_req.json()
#get number of party members who served after 1996 from the json reply
    num_resp = float(num_json['count'])
    resp_per_page = num_json['page']['per_page']
#calculate the number of pages of responses that need to be read
    num_pages = int(math.ceil(num_resp/resp_per_page))
#set initial parameters for for loop
    bio_req['fields'] = 'bioguide_id'
#retrieve all the bioguide_ids for party legislators and store them
    bio_id_lst = []
    for i in range(1,num_pages+1):
        bio_req['page'] = i
        bio_iter = requests.get(url,params=bio_req)
        req_json = bio_iter.json()
        for bio_id in req_json['results']:
            bio_id_lst.append(bio_id['bioguide_id'])
    return bio_id_lst
rep_bio_ids = get_leg_ids('R')
dem_bio_ids = get_leg_ids('D')
'''a function to create a list of most common words when passed a list of 
legislator ids'''
def get_word_lst(ids):
    url='http://capitolwords.org/api/1/phrases.json'
    #set parameters for the api request
    req_param = {'apikey':api_key,'entity_type':'legislator',
                 'sort':'tfidf desc'}
    phrase_lst = []
    #iterate over the input list of legislator ids
    for id in ids:
        req_param['entity_value'] = id
        phrase_req = requests.get(url, params=req_param)
        reply_json = phrase_req.json()
        #iterate over the output json and write the first 100 replies to a list
        for line in reply_json:
            phrase_lst.append(line['ngram'])
    return phrase_lst
rep_tot_words = get_word_lst(rep_bio_ids)
dem_tot_words = get_word_lst(dem_bio_ids)
rep_words = list(set(rep_tot_words)-set(dem_tot_words))
dem_words = list(set(dem_tot_words)-set(rep_tot_words))
top_rep_words = Counter(rep_words).most_common()
top_dem_words = Counter(dem_words).most_common()