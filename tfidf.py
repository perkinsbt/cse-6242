# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 12:45:23 2016

@author: Perk
"""
import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(input='filename',stop_words='english',
                        ngram_range=(1,5),max_features=50000)
npr_dir = 'npr articles/npr articles/'
npr = os.listdir(npr_dir)
files = []
for file in npr:
    files.append(npr_dir + file)
tfs = tfidf.fit_transform(files)
feature_names = tfidf.get_feature_names()
dense = tfs.todense()
phrase_dict = {}
for i in range(len(dense.tolist())):
    article = dense[i].tolist()[0]
    phrase_scores = [pair for pair in 
    zip(range(0, len(article)),article) if pair[1]>0]
    sorted_phrase_scores = sorted(phrase_scores, key=lambda x: x[1],
                                  reverse=True)
    top_phrases = [(feature_names[word_id], score) for (word_id,score) in 
    sorted_phrase_scores][:10]
    phrase_dict[npr[i]] = top_phrases
with open('top_article_phrases.json','w') as outfile:
    json.dump(phrase_dict,outfile)