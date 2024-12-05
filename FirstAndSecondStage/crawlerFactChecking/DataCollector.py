# Fact-checking collector
import pandas as pd
import feedparser
import xml.sax.saxutils as saxutils
import ast
import re
from bs4 import BeautifulSoup
from datetime import date
import requests
#Jeferson Begin
import urllib.parse
from pkg_resources._vendor.jaraco.functools import except_
import json
#Jeferson End
    
class DataCollector:

#Jeferson Begin
    urllib.parse.quote(':')
#Jeferson End

    def __init__(self):
        pass

    def loadFile(name):
        return pd.read_csv("./Dataset/" + name + ".csv", header = 0, index_col=False, sep=',')

    def collectLinksFromFeed(url):
        
#Jeferson Begin
        is_https = "https://" in url[:len("https://")]
        
        if is_https:
          feed_content = requests.get(url)
          feed = feedparser.parse(feed_content.text)
        elif not is_https:
          feed = feedparser.parse(url)
        
        #print(feed)
    
    
        #d = feedparser.parse(url)        
        links = []
        for entry in feed.entries: links.append(entry.link)
        return links    
#Jeferson End        
        




    def saveFile(data, name):
        data.to_csv("./Dataset/" + name + ".csv", encoding='utf-8-sig', index=False)

    def updateFile(oldFile, additions):
        temp = pd.concat([oldFile, additions], ignore_index=True)
        temp = temp.drop_duplicates(keep='first', subset=['claimReviewed'])
        count=1
        for index, row in temp.iterrows():
            #temp.set_value(index,'id', count)
            temp.at[index,'id'] = count
            count=count+1
        return temp
    
    def re_char(str):
        return re.sub('[^A-Za-z0-9 \!\@\#\$\%\&\*\:\,\.\;\:\-\_\"\'\]\[\}\{\+\á\à\é\è\í\ì\ó\ò\ú\ù\ã\õ\â\ê\ô\ç\|]+', '',str)

    def preProcessing(str): 
        newString = saxutils.unescape(str.replace('&quot;', ''))
        newString = re.sub('[^A-Za-z0-9 \!\@\#\$\%\&\*\:\,\.\;\:\-\_\"\'\]\[\}\{\+\á\à\é\è\í\ì\ó\ò\ú\ù\ã\õ\â\ê\ô\ç\|]+', '',newString)
        newDict = ast.literal_eval(newString)
        #jeferson atenção
        if "@graph" in newDict:
            newDict = newDict['@graph'][0]        
        return newDict

    def collectData(url, type):
        response = requests.get(url, timeout=30)
        content = BeautifulSoup(response.content, "html.parser")
        allData = []
        if (type=="virtualMedia"):
            try:                
                element = []
                element.append("99999999")
                element.append(url)
                element.append("Mídia Convencional")
                element.append(date.today())
                element.append(DataCollector.re_char(content.title.get_text().replace('<title>','').replace('</title>','')))
                element.append(DataCollector.re_char(content.title.get_text().replace('<title>','').replace('</title>','')))
                element.append(DataCollector.re_char(content.title.get_text().replace('<title>','').replace('</title>','')))
                element.append("6")
                element.append("5")
                element.append("VERDADEIRO")
                allData.append(element)
                return allData
            except:
                pass 
          
        for claimReview in content.findAll('script', attrs={"type": "application/ld+json"}):
#        for claimReview in content.findAll('script', attrs={"type": "application/json-ld"}):            
            
            element = []
            try:
                claimDict = DataCollector.preProcessing(claimReview.get_text(strip=True))
                element.append("99999999")
                element.append(url)
                
                #Jeferson Begin
                #element.append(claimDict['author']['url'])
                element.append(claimDict['author'])
                #element.append(claimDict['itemReviewed']['@type'])
                #Jeferson End
                
                element.append(claimDict['datePublished'])
                   
                #Jeferson Begin
                try: element.append(claimDict['claimReviewed'])                
                except:   
                    element.append(DataCollector.re_char(content.title.get_text().replace('<title>','').replace('</title>','')))
   
                   
                #if (claimDict['claimReviewed']):
                #    element.append(claimDict['claimReviewed'])
                #else:   
                #    element.append(DataCollector.re_char(content.title.get_text().replace('<title>','').replace('</title>','')))
                #Jeferson End
                   
                try: element.append(claimDict['reviewBody'])
                except:
                    try:
                        element.append(claimDict['description'])
                    except:
                        element.append('Empty')
                element.append(DataCollector.re_char(content.title.get_text().replace('<title>','').replace('</title>','')))
                element.append(claimDict['reviewRating']['ratingValue'])
                element.append(claimDict['reviewRating']['bestRating'])
                print(claimDict['reviewRating']['alternateName'])
                if ( (claimDict['reviewRating']['alternateName']) == "não_é_bem_assim"):
                    element.append('FALSO')
                else:    
                    element.append(claimDict['reviewRating']['alternateName'])               
                
                allData.append(element)                
 
            except:
                pass
        return allData

    @staticmethod
    def collect(agencies, virtualMedias, toprow):
        
        linksAgenciesList = []
        linksVirtualMediasList = []
        #Get links list of the Agencies
        for url in agencies: linksAgenciesList.extend(DataCollector.collectLinksFromFeed(url))
        #Get links list of the Virtual Medias
        for url in virtualMedias: linksVirtualMediasList.extend(DataCollector.collectLinksFromFeed(url))
        print ("Number of Agencies links: {}".format(len(linksAgenciesList)))
        print ("Number of Virtual Medias links: {}".format(len(linksVirtualMediasList)))

        #Get ClaimReview of the news
        claimList = []
        count = 0
        for url in linksAgenciesList:
            count = count + 1
            print ("{} de {} > ".format(count,len(linksAgenciesList)) + url)
            lineList = DataCollector.collectData(url,"agency")
            for line in lineList: claimList.append(line)
            print ("Das {} noticias de agências somente {} tem claimReview > ".format(len(linksAgenciesList),len(claimList)) )   
        #Jeferson Begin
        print ("Das {} noticias de agências somente {} tem claimReview > ".format(len(linksAgenciesList),len(claimList)) )   
        
        #Jeferson End  
          
        count=0
        for url in linksVirtualMediasList:
            count = count + 1
            print ("{} de {} > ".format(count,len(linksVirtualMediasList)) + url)
            lineList = DataCollector.collectData(url,"virtualMedia")
            for line in lineList: claimList.append(line)

        #Jeferson Begin
        print ("Das {} somente {} tem avaliação > ".format(len(linksVirtualMediasList),len(claimList) ) )   
        #Jeferson End  
                    
        additions = pd.DataFrame(claimList, columns=toprow)

        oldFile = DataCollector.loadFile('LabeledNews')
        process1Update = DataCollector.updateFile(oldFile, additions)
        DataCollector.saveFile(process1Update, 'LabeledNews')
        
