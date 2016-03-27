# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 22:26:39 2016

@author: katherinemckenna
"""

api_key="MDIzNDQ2MzI0MDE0NTkwOTUyMjU3YzE3Zg000"

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
    

beginning_url="http://api.npr.org/query?"
term1="apiKey="+api_key
term2="&searchTerm=death%20tax"
#not working - term3="&id=455776378,1014,455779148,455779263,455779709,455779583" ##this searches political stories
term4="&output=JSON"
term5="&fields=textWithHtml,relatedLink,transcript"
terms=term1+term2+term4+term5

url=beginning_url+terms
out=req(url)

#http://api.ft.com/content/items/v1/834ffdf2-728c-11e1-9be9-00144feab49a?apiKey=yourApiKey 
#searchTerm=Mitt%20Romney&dateType=story&output=JSON&apiKey=MDIzNDQ2MzI0MDE0NTkwOTUyMjU3YzE3Zg000