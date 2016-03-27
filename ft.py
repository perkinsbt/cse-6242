# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 22:26:39 2016

@author: katherinemckenna
"""

api_key="ebyu6ahpnep8yeye4ydwy8gf"

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
    

beginning_url="http://api.ft.com/content/items/v1/834ffdf2-728c-11e1-9be9-00144feab49a?"
term1="apiKey="+api_key
terms=term1

url=beginning_url+terms
out=req(url)

#http://api.ft.com/content/items/v1/834ffdf2-728c-11e1-9be9-00144feab49a?apiKey=yourApiKey 