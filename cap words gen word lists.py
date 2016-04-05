# -*- coding: utf-8 -*-
"""
This file will generate lists of the most commonly used words by Republicans
and Democrats
"""
import requests
api_key = open('sunlight API.txt','r')
rep_bio_req = {'party':'R','fields':'bioguide_id','all_legislators':'true',
               'term_start__gte':'1996-01-01','apikey':api_key}
rep_bio_id = requests.get(
    'https://congress.api.sunlightfoundation.com/legislators',
    params=rep_bio_req)
#print(rep_bio_id.url)
rep_bio_json = rep_bio_id.json()
api_key.close()