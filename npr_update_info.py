# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 11:56:59 2016

@author: katherinemckenna
"""

import csv
import os
import re
import pandas as pd
os.chdir("/Users/katherinemckenna/Documents/CSE6242/Project/Articles Pulling")

csvfile="/Users/katherinemckenna/Documents/CSE6242/Project/Articles Pulling/ArticleInfo copy 2.csv"
info=[]
with open(csvfile, "r") as input_file:
    inforeader = csv.reader(input_file)
    for row in inforeader:
        info.append(row)

author=[]
date=[]
show=[]
articleid=[]
title=[]        
for i in range(len(info)):
    a=info[i]
    a=a[0]
    
    #get author first
    p = re.compile('\[(.*?)\]')
    m=p.search(a)
    byline=a[m.start():m.end()]
    author.append(byline)
    
    ##get date
    p=re.compile('\d\d \w\w\w \d\d\d\d')
    m=p.search(a)
    date_full=a[m.start():m.end()]
    date.append(date_full)
    
    ##get show
    p=re.compile('\d\d\', ')
    m=p.search(a)
    start=m.end()  
    p=re.compile('\w\', \d')
    m=p.search(a)
    end=m.start()
    show.append(a[start:end+1])
    
    ##get article id
    articleid.append(i)
    
    ##get article title
    p=re.compile('\$text\': ')
    m=p.search(a)
    start=m.end()
    
    p=re.compile('\}')
    m=p.search(a)
    end=m.start()
    
    title.append(a[start:end])


for i in range(len(show)):
    show2=show[i]
    show2=show2[2:len(show2)]
    if len(show2)==0:
        a=0
    elif (show2[len(show2)-1]=="'" and show2[0]=="'"):      
        show2=show2[1:len(show2)-1]
        show[i]=show2
    elif show2[0]=="'":
        show2=show2[1:len(show2)]
        show[i]=show2
    elif show2[len(show2)-1]=="'":
        show2=show2[0:len(show2)-1]
        show[i]=show2
    else:
        show[i]=show2
        
for i in range(len(title)):
    title2=title[i]
    title2=title2[2:len(title2)]
    if len(title2)==0:
        a=0
    elif (title2[len(title2)-1]=="'" and title2[0]=="'"):      
        title2=title2[1:len(title2)-1]
        title[i]=title2
    elif title2[0]=="'":
        title2=title2[1:len(title2)]
        title[i]=title2
    elif title2[len(title2)-1]=="'":
        title2=title2[0:len(title2)-1]
        title[i]=title2
    elif title2[len(title2)-1]=="\"":
        title2=title2[0:len(title2)-1]
        title[i]=title2   
    else:
        title[i]=title2

article_list = pd.DataFrame({'show' : show,
 'date' : date,
 'title':title,'articleid':articleid
  })

article_list.to_csv("Article Info_Cleaned.csv")

##for multiple authors, expand the data
new_article_id=[]
new_author=[]
for i in range(len(articleid)):
    author2=author[i]
    several=author2.split(",")
    for j in range(len(several)):
        if (len(several)==1):
            author3=several[j]
            author3=author3[1:len(author3)-1]
            author3=author3
            new_author.append(author3)
            new_article_id.append(articleid[i])
        elif (j==0):    
            author3=several[j]
            author3=author3[1:len(author3)]
            author3=author3
            new_author.append(author3)
            new_article_id.append(articleid[i])
        elif(j==len(several)-1):
            author3=several[j]
            author3=author3[0:len(author3)-1]
            author3=author3
            new_author.append(author3)
            new_article_id.append(articleid[i])
        else:
            author3=several[j]
            author3=author3
            new_author.append(author3)
            new_article_id.append(articleid[i])

for i in range(len(new_author)):
    author4=new_author[i]
    author4=author4[2:len(author4)]
    if len(author4)==0:
        a=0
    elif (author4[len(author4)-1]=="'" and author4[0]=="'"):      
        author4=author4[1:len(author4)-1]
        new_author[i]=author4
    elif author4[0]=="'":
        author4=author4[1:len(author4)]
        new_author[i]=author4
    elif author4[len(author4)-1]=="'":
        author4=author4[0:len(author4)-1]
        new_author[i]=author4
    else:
        new_author[i]=author4
        
    
    
author_list = pd.DataFrame({'articleid' : new_article_id,
 'author' : new_author
  })
  
  
author_list.to_csv("Author Info_Cleaned.csv")
