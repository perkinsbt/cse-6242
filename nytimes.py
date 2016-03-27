# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 22:26:39 2016

@author: katherinemckenna
"""

api_key="0358c9b864c6cad5603a6a32420c60be:7:74784865"

import urllib2
import json

#Helper function to read the API
def req(url):
    conn = urllib2.urlopen(url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()
    return response
    

beginning_url="http://api.nytimes.com/svc/search/v2/articlesearch.json?"
term1="api-key="+api_key
term2="&begin_date=20000101"
term3="&sort=oldest"
term4="&fl=print_page,_id,word_count,snippet,web_url"
terms=term1+term2+term3+term4

url=beginning_url+terms
out=req(url)
