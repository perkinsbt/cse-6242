# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 12:45:23 2016

@author: Perk
"""
import os
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(input='filename',stop_words='english',
                        ngram_range=(1,5))
npr_dir = 'npr articles/npr articles/'
npr = os.listdir(npr_dir)
files = []
for file in npr:
    files.append(npr_dir + file)
tfs = tfidf.fit_transform(files)
feature_names = tfidf.get_feature_names()
dense = tfs.todense()
article = dense[0].tolist()[0]
phrase_scores = [pair for pair in 
zip(range(0, len(article)),article) if pair[1]>0]

