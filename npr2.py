# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 11:05:35 2016

@author: katherinemckenna
"""

from urllib2 import Request, urlopen
import json

articlecount = 0
articleid=0
list_info=[]
for j in range(1001,2500): 
    try:
        nprurlfull = 'http://api.npr.org/query?id=1014&http://api.npr.org/query?id=1149,1126,1059,1006,1095,1058,1060,1017,1013,139482413,1131,1025,1124,1031,1128,1027,1022,1010,1101,1127,1070,1020,1009,1122,1001,1150,1028,1133,1057,455776378,455778960,1014,455779148,455779263,455779709,455779583,1048,1015,1016,1024,1007,1090,1019,1078,1003,1004,1066&fields=text,title,storyDate,show,byline&startDate=2015-04-15&endDate=2016-04-15&startNum='+str(j)+'&dateType=story&sort=dateAsc&output=JSON&numResults=20&searchType=fullContent&apiKey=MDIzNDQ2MzI0MDE0NTkwOTUyMjU3YzE3Zg000'
        requestfull = Request(nprurlfull)
        articles = json.loads(urlopen(requestfull).read())
        count = len(articles['list']['story'])
        articlecount += count
        for article in articles['list']['story']: #for each article in the timeline
            title=article.get('title')   
            author=article.get('byline')
            auth_list=[]
            if author is None:
                pass
            else:
                for i in range(len(author)):
                    a=author[i]
                    auth_list.append(a['name']['$text'])
            show=article.get('show') 
            if show is None:
                pass
            else:
                s=article.get('show')
                s=s[0]
                s=s['program']['$text']
            date=article.get('storyDate')
            date=date['$text']
            art = article.get('text') #drill down
            testvals = art.get('paragraph') #drill down to text
            par=""
            for i in testvals: #grab text for each paragraph, convert to utf8, then append to initialized lis
                piece = i.get('$text')
                if piece is None:
                    pass
                else:
                    piece = piece.encode('utf8')
                    par=par+" "+piece
            if par[0:11]==" [Copyright":
                pass
            else:
                articleid=articleid+1
                file="npr"+"_"+str(articleid)+".txt"
                info=(auth_list,date,s,articleid,title)
                list_info.append(info)
                with open(file,"ab") as f:
                    f.write(str(par))
                
    except ValueError:
        pass
    print j

csvfile="/Users/katherinemckenna/Documents/CSE6242/Project/Articles Pulling/ArticleInfo.csv"
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in list_info:
        writer.writerow([val])  