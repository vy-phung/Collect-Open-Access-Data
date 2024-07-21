import pandas as pd
from CollectData.DefaultPackages import openFile
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collection import Counter
from CollectData.source import GetText

'''A paper keywords in title or abstract, sometimes the title maximum words are 10'''
class keywords():
    def __init__(self, title, abstract):
        self.title = openFile.openFile(title) 
        self.abstract = openFile.openFile(abstract)
        self.text = self.title + self.abstract
    def topCommonKeywords(self):
        '''maybe try NLP for query understanding:
        consider synonyms, context, linguistic variations
        improve the accuray of search results'''
        topKey = {}
        # use machine learning and return 3 top common ones
        '''Shorter content (300-500 words): 1 primary keyword, 2-3 secondary keywords
        Medium content (500-800 words): 1 primary keyword, 3-4 secondary keywords
        Longer content (800+ words): 1 primary keyword, 5-6 secondary keywords'''
        '''Length of title: max about 10 words
        Length of abstract: max about 300 words'''
        # remove stopwords
        #nltk.download('stopwords')
        stopWords = set(stopwords.words('english'))
        # filter title
        textWords = word_tokenize(self.text.lower())
        filteredWord = [w for w in textWords if not w in stopWords]
        # count the top significant words
        for word in filteredWord: 
            topKey[word] = textWords.count(word)
        # create keywords from common keywords of title and abstract
        while len(topKey) > 5:
            # if length of topKey is more than 5, then takes the 50% of the highest occurences
            # sort descending so that the highest at top
            sortedTopKey = sorted(topKey.items(), key=lambda x:x[1], reverse=True)
            topKey = dict(sortedTopKey[:int(len(sortedTopKey)/2)])
        keyWords = 'AND'.join(list(topKey.keys()))
        return keyWords
    def searchKeywords(self,keyword, source):
        # use that keyword to search for how many data can collect from it
        # call the class GetText from source to search the keyword
        saveOutput = ''
        Format = ''
        GT = GetText(keyword, saveOutput, Format)
        # decide which source I want to use to search for my keywords
        if source == "NCBI":
            text = GT.EntrezDirect()
        elif source == "Web Scrape":
            text = GT.webScraping()
        # the text returned here is the data getting from searchin keywords
        return text         
    def specificKeywords(self):
        return ''
    def getReferenceKey(self):
        '''I can create the list of reference links for customers to refer. I can also give them the image or information of my max heap to see the top citations and
        they can use these citations to cite in their papers'''
        '''I can try search engine method to get the reference key which means from one site
        refers to another site:
        + web crawler: These crawlers follow links from one page to another, indexing the content of each page they visit
        + index: 
        + ranking: RankNet or LambdaMART which are ML'''
        # try PageRank algorithm
        
        return ''        

'''References: 
https://www.geeksforgeeks.org/removing-stop-words-nltk-python/'''