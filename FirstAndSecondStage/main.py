import sys
import pandas as pd
import feedparser
import xml.sax.saxutils as saxutils
import ast
import re
from bs4 import BeautifulSoup
import requests
import crawlerFactChecking as fact
import csv
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

#Jeferson Begin
import tweepy
from argon2._utils import Parameters

from twarc import Twarc2, expansions
#from twarc import Twarc

import datetime
import json


import requests
import os
#Jeferson End

if sys.version_info[0] >= 3:
    import crawlerTwitterWeb as craw
else:
    sys.exit()
    

def main():
	#Imput parameters
    agencies = ["https://aosfatos.org/noticias/feed/", 
                "https://piaui.folha.uol.com.br/lupa/feed/",              
                "https://g1.globo.com/fato-ou-fake/",
                "https://www.e-farsas.com/",
                "https://www.boatos.org",            
                "https://apublica.org/feed/", 
                "https://apublica.org/tag/truco/feed/",
                "https://checamos.afp.com"]  
#    virtualMedias = ["https://g1.globo.com/rss/g1/tecnologia/", "https://g1.globo.com/rss/g1/educacao/", "https://g1.globo.com/rss/g1/economia/","https://noticias.r7.com/feed.xml"]
    virtualMedias = ["https://g1.globo.com/rss/g1/tecnologia/", "https://g1.globo.com/rss/g1/educacao/", "https://g1.globo.com/rss/g1/economia/"]
    toprow = ['id','URL', 'Author', 'datePublished', 'claimReviewed', 'reviewBody', 'title', 'ratingValue', 'bestRating', 'alternativeName']
    newStopWords = ['#Verificamos:','Checamos','Agência','Lupa','Pública','Aos','Fatos','fatos','Fake','FAKE','fake',',',':',';','mentira','verdade','falso','.','O','A','Os','As','Em','Na', 'No', '|', 'G1', 'g1']
    language = 'portuguese'
    since = "2023-04-04"
    until = "2023-07-04"
    maxTweets = 10000
    
    #Jeferson Begin 
    #Tweet API Parameters 
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAPhyYAEAAAAAYH4N4DZ1LLq1w1bIydzt%2BxPt7Cw%3DWDais89jJ7wobYF5GKRljdXbzSoyowlvX83oj4gtmZTLx8tf77"
    #Jeferson End
    
       
	#Stage 1 - Identify Labeled News
    #fact.DataCollector.collect(agencies, virtualMedias, toprow)

    #Stage 2 - Connect News with Propagation
    dataset = pd.read_csv("./Dataset/LabeledNews.csv", index_col=0, header = 0)
    toprow = ['id','news_url','title','tweet_ids']
    stop_words = set(stopwords.words(language)) 
    stop_words = stop_words.union(newStopWords)
    newsListFake = []
    newsListNotFake = []    
    for index, row in dataset.iterrows():
        word_tokens = word_tokenize(row[3])   
        filtered_sentence = []   
        for w in word_tokens: 
            if w not in stop_words: 
                filtered_sentence.append(w)
        filtered_sentence = [ele for ele in filtered_sentence if not ele.startswith("'")]    
        query = "abcekrkrmmtre bcertkmrekd cderektmrelkm deflkermt efgerktmrelk fghkerltrlket ghilerkngtlekrntlke"
        if (len(filtered_sentence) >=  60):
            filtered_sentence = filtered_sentence[0:15]
            query = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', str(filtered_sentence))
        elif (len(query) >=  30):
            filtered_sentence = filtered_sentence[0:10]
            query = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', str(filtered_sentence))
        elif (len(query) >= 8):
            filtered_sentence = filtered_sentence[0:8]
            query = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', str(filtered_sentence))

        print (query)
      

        #Jeferson Begin
        # Método de busca Twarc2 - Begin
        client = Twarc2(bearer_token=bearer_token)
        # Specify the start time in UTC for the time period you want Tweets from
        start_time = datetime.datetime(2023, 4, 11, 0, 0, 0, 0, datetime.timezone.utc)
        
        # Specify the end time in UTC for the time period you want Tweets from
        end_time = datetime.datetime(2023, 7, 4, 0, 0, 0, 0, datetime.timezone.utc)    
        
        query = query
        
        # The search_all method call the full-archive search endpoint to get Tweets based on the query, start and end times
        # search_results = client.search_all(query=query, start_time=start_time, end_time=end_time, max_results=100)
        Texto = {"text": "Hello world!"}   
        #client.add_stream_rules([{"value": "hey", "tag": "twarc-test"}, {"value": "joe", "tag": "twarc-test"}])     
        #client.post("https://api.twitter.com/2/tweets", json_data = Texto)
        #client.user_lookup(users, usernames, expansions, tweet_fields, user_fields)
        users_found = 0
        usernames = ["jefluisgon", "barackobama", "rihanna"]
        
       
        for user in client.user_lookup(users=usernames, usernames=True):
            print(user['screen_name'])
    
        #for response in client.user_lookup(usernames, usernames=True):
        #    for profile in response["data"]:
        #        users_found += 1
        #assert users_found == 3
        
        # Método de busca Twarc2 - End
        #Jeferson End


  #=============================================================================
  #       #Jeferson Begin        
  #       # via método Tweepy
  #       client = tweepy.Client(bearer_token)
  #       # Search Recent Tweets
  #       # This endpoint/method returns Tweets from the last seven days
  #        # You can retrieve up to XX Tweets by specifying max_results
  #       response = client.search_all_tweets(query=query, max_results=500)
  #       # The method returns a Response object, a named tuple with data, includes,
  #       # errors, and meta fields
  #       print(response.meta)
  # 
  #       # In this case, the data field of the Response returned is a list of Tweet
  #       # objects
  #       tweets = response.data
  #       #Jeferson End
  #=============================================================================
        


 
 #==============================================================================
 #        # To set your environment variables in your terminal run the following line:
 #        # export 'BEARER_TOKEN'='<your_bearer_token>'
 #        #bearer_token = os.environ.get("AAAAAAAAAAAAAAAAAAAAAPhyYAEAAAAAKBoOX9vX5NuvGmD%2B393KtNw%2FpX8%3D4U5D6WTD3aJ4DorWWRAIuhmqIUUVhzaSFLAdpVbSVOaNocwwex")
 #        search_url = "https://api.twitter.com/2/tweets/search/all"
 #         
 #        # Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
 #        # expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
 #        query_params = query
 # 
 #        def bearer_oauth(r):
 #            """
 #            Method required by bearer token authentication.
 #            """
 #         
 #            r.headers["Authorization"] = f"Bearer {bearer_token}"
 #            r.headers["User-Agent"] = "v2FullArchiveSearchPython"
 #            return r
 #         
 #         
 #        def connect_to_endpoint(url, params):
 #            response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
 #            print(response.status_code)
 #            if response.status_code != 200:
 #                raise Exception(response.status_code, response.text)
 #            return response.json()
 # 
 # 
 #        json_response = connect_to_endpoint(search_url, query_params)
 #        print(json.dumps(json_response, indent=4, sort_keys=True))
 #==============================================================================


#===============================================================================
#  
#         #Jeferson Begin
#         # Método de busca Twarc2 - Begin
#         client = Twarc2(bearer_token=bearer_token)
#        # Specify the start time in UTC for the time period you want Tweets from
#         start_time = datetime.datetime(2023, 4, 11, 0, 0, 0, 0, datetime.timezone.utc)
#     
#         # Specify the end time in UTC for the time period you want Tweets from
#         end_time = datetime.datetime(2023, 7, 4, 0, 0, 0, 0, datetime.timezone.utc)    
#       
#         query = query
#     
#         # The search_all method call the full-archive search endpoint to get Tweets based on the query, start and end times
#         # search_results = client.search_all(query=query, start_time=start_time, end_time=end_time, max_results=100)
#         search_results = client.search_recent(query=query, start_time=start_time, end_time=end_time)
#             
#         # Twarc returns all Tweets for the criteria set above, so we page through the results
#         for page in search_results:
#             # The Twitter API v2 returns the Tweet information and the user, media etc.  separately
#             # so we use expansions.flatten to get all the information in a single JSON
#             result = expansions.flatten(page)
#             
#             concTweet = ""
#             aux = row[8]
#             
#             for tweet in result:
#                 # Here we are printing the full Tweet object JSON to the console
#                 print(json.dumps(tweet))                
# 
#                 #print(tweet["text"])
#                 if (concTweet != ""):
#                     concTweet = concTweet + str("\t") + str(tweet["id"])
#                 else:
#                     concTweet = str(tweet["id"])
#                 
#             line = []            
#             line.append(index)
#             line.append(row[0])
#             line.append(row[3])
#             line.append(concTweet)
#             if (aux.upper()=="FALSO"):
#                 newsListFake.append(line)
#             elif (aux.upper()=="VERDADEIRO"):
#                 newsListNotFake.append(line)
#      
#         # Método de busca Twarc2 - End
#         #Jeferson End
#         
#===============================================================================

#===============================================================================
#         # Método Original - Begin
#         # Este metódo é baseado em pesquisar tweets por URL
#         #Searching in twitter
#         tweetCriteria = craw.manager.TweetCriteria().setQuerySearch(query +" -fake -filter:replies").setSince(since).setUntil(until).setMaxTweets(maxTweets)
#         tweets = craw.manager.TweetManager.getTweets(tweetCriteria)
# 
#         concTweet = ""
#         aux = row[8]
#         if tweets is not None:            
#             for tweet in tweets:
#                 print(tweet.text)
#                 if (concTweet != ""):
#                     concTweet = concTweet + str("\t") + str(tweet.id)
#                 else:
#                     concTweet = str(tweet.id)
#                  
#             line = []            
#             line.append(index)
#             line.append(row[0])
#             line.append(row[3])
#             line.append(concTweet)
#             if (aux.upper()=="FALSO"):
#                 newsListFake.append(line)
#             elif (aux.upper()=="VERDADEIRO"):
#                 newsListNotFake.append(line)
#         # Método Original - End
#===============================================================================
                    
    process2ResultFake = pd.DataFrame(newsListFake, columns=toprow)
    process2ResultNotFake = pd.DataFrame(newsListNotFake, columns=toprow)
    process2ResultFake = process2ResultFake.set_index('id')
    process2ResultNotFake = process2ResultNotFake.set_index('id')
    process2ResultFake.to_csv("./Dataset/News_fake.csv", encoding='utf-8-sig', index=True)
    process2ResultNotFake.to_csv("./Dataset/News_notFake.csv", encoding='utf-8-sig', index=True)

if __name__ == '__main__':
    main()
