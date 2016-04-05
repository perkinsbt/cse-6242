# -*- coding: utf-8 -*-
"""
This file will generate lists of the most commonly used words by Republicans
and Democrats.  You need a valid API key and to save the API key in the file
'sunlight API.txt' in the same directory as this .py file.
"""
import requests
import math
#reads the API key
with open('sunlight API.txt','r') as api_file:
    api_key = api_file.read()
'''search parameters for finding the number of Republicans whose terms began
after 1996'''
def get_leg_ids(party):
    url='https://congress.api.sunlightfoundation.com/legislators'
    bio_req = {'party':party,'fields':'count','all_legislators':'true',
               'term_start__gte':'1996-01-01','apikey':api_key}
    num_req = requests.get(url, params=bio_req)
    num_json = num_req.json()
#number of Republicans who served after 1996
    num_resp = float(num_json['count'])
    resp_per_page = num_json['page']['per_page']
#calculate the number of pages of responses that need to be read
    num_pages = int(math.ceil(num_resp/resp_per_page))
#set initial parameters for for loop
    bio_req['fields'] = 'bioguide_id'
#retrieve all the bioguide_ids for Republican legislators and store them
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