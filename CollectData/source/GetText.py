import os
from CollectData.keyword import findKeywords
from CollectData.DefaultPackages import openFile
import requests
# pip install google
import google  
from googlesearch import search 
# pip install bs4
from bs4 import BeautifulSoup

class GetText():
    def __init__(self, keyword, saveOutput, format):
        self.keyword = keyword
        self.saveOutput = saveOutput
        self.format = format
    def EntrezDirect(self): # search by using ED
        # NCBI from US
        commandLine = 'source CollectData/source/NCBI/EntrezDirectNCBI.sh; download' + self.keyword + self.saveOutput + self.format
        # run entrez direct and then open the saved file as text
        os.system(commandLine)
        text = openFile.openFile(self.saveOutput)
        return text
    def BOLD(self): # barcode of life data system
        # BOLD from Canada
        # https://www.boldsystems.org/index.php/
        None
    def webScraping(self):
        # search by the keyword and then get the link from that keyword to do webscraping
        # from the link try each link to get the good content        
        query = self.keyword
        canGetAPI = []
        notAccess = []
        for link in search(query, tld="co.in", num=10, stop=10, pause=2):
            getLink = requests.get(link)
            statusCode = getLink.status_code
            if str(statusCode) == "200":
                canGetAPI.append(link)
                # classify HTML text and JSON file
                # for HTML text, then do web harvest here
                try: # get json file
                    APIs = dict(getLink.json())
                    GT = GetText(self.keyword,self.saveOutput,self.format)
                    request = ''
                    info = GT.API(APIs,request)
                except: # html so do web harvest
                    text = getLink.text     
                    soup = BeautifulSoup(text, "html.parser")
                    for child in soup.descendants:
                        if child.name:
                            if soup.child.name.text == self.keyword:
                                info = soup.child.name.text
            elif str(statusCode)[0] == "4": # means it is "4xx"
                notAccess.append(link)
            elif str(statusCode) == '503': # the server not ready to handle the request
                print("server not ready to handle request")
            elif str(statusCode) == '301':
                print("domain/endpoint name is changed")

        return info
    def API(self, APIs, request):
        # get data from API
        return ''
    def reference(self, refer):
        Refs = {}
        text = ''
        return text