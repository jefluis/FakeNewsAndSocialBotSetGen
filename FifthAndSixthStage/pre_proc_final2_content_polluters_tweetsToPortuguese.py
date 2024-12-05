# -*- coding: utf-8 -*-
"""
Created on October 07 2023

@author: Jeferson Luis Gonçalves
"""

import pymysql
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

from mtranslate import translate
from googletrans import Translator
import translators as ts
from deep_translator import (GoogleTranslator,
                             ChatGptTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator,
                             DeeplTranslator,
                             QcriTranslator,
                             single_detection,
                             batch_detection)

import datetime
import time
import random


#Traduzir para português
def TranslateToPt(Tweet):  
    numero = random.randint(1, 7)
    #print('Número:  ', numero)
    if numero == 1 or numero == 2:
        #Mtranslate  
        try:  
            translated_text = translate(Tweet, 'pt')
        except Exception as eTranslate:
            print("Exceção ocorrida na tradução número {} , mensagem de erro {} /n tweet {}".format(numero, eTranslate, Tweet))
             
            return Tweet  
        return translated_text    

    #===========================================================================
    # if numero == 2 or numero == 3 :        
    #     #https://pypi.org/project/googletrans/
    #     translator = Translator()
    #     translator.raise_Exception = True;
    #     try:
    #         translation = translator.translate(Tweet, dest='pt')
    #     except Exception as eTranslate:
    #         print("Exceção ocorrida na tradução número {} , mensagem de erro {}".format(numero, eTranslate))
    #         return Tweet    
    #    
    #     return translation.text
    #===========================================================================
    
    #===========================================================================
    # if numero == 3: 
    #     #Translators (Bing) - import translators as ts
    #     try:         
    #         return ts.translate_text(query_text=Tweet, translator = 'bing', from_language = 'auto', to_language = 'pt')
    #     except Exception as eTranslate:
    #         print("Exceção ocorrida na tradução número {} , mensagem de erro {}".format(numero, eTranslate))
    #         return Tweet  
    #===========================================================================
    
    if numero == 4 or numero == 3:        
        #Translators (Google) - import translators as ts
        try: 
            return ts.translate_text(query_text=Tweet, translator = 'google', to_language = 'pt')
        except Exception as eTranslate:
            print("Exceção ocorrida na tradução número {} , mensagem de erro {} /n tweet {}".format(numero, eTranslate, Tweet))
            return Tweet  
        
    if numero == 5 or numero == 6:        
        #Translators (baidu) - import translators as ts
        try: 
            return ts.translate_text(query_text=Tweet, translator = 'baidu', to_language = 'pt')
        except Exception as eTranslate:
            print("Exceção ocorrida na tradução número {} , mensagem de erro {} /n tweet {}".format(numero, eTranslate, Tweet))
            return Tweet  
        
    #===========================================================================
    # if numero == 6:
    #     #Translators (papago) - import translators as ts
    #     try: 
    #         return ts.translate_text(query_text=Tweet, translator = 'papago', to_language = 'pt')
    #     except Exception as eTranslate:
    #         print("Exceção ocorrida na tradução número {} , mensagem de erro {}".format(numero, eTranslate))
    #         return Tweet  
    #===========================================================================

    if numero == 7:
        #deep_translator (Google Translator)
        try: 
            translated = GoogleTranslator(source='auto', target='pt').translate(Tweet)
            
        except Exception as eTranslate:
            print("Exceção ocorrida na tradução número {} , mensagem de erro {} /n tweet {}".format(numero, eTranslate, Tweet))
            return Tweet  

        return translated

    #===========================================================================
    # if numero == 8:
    #     #deep_translator (My Memory Translator)
    #     try: 
    #         translated = MyMemoryTranslator(source='english', target='portuguese').translate(Tweet)
    #    
    #     except Exception as eTranslate:
    #         print("Exceção ocorrida na tradução número {} , mensagem de erro {}".format(numero, eTranslate))
    #         return Tweet  
    #     
    #     return translated
    # 
    # if numero == 9:    
    #     #deep_translator (ChatGPT_Translator)
    #     try: 
    #         translated = ChatGptTranslator(api_key='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', target='portuguese').translate(Tweet)
    #     except Exception as eTranslate:
    #         print("Exceção ocorrida na tradução número {} , mensagem de erro {}".format(numero, eTranslate))
    #         return Tweet  
    #     
    #     return translated
    #===========================================================================
    
    
#Construindo função para receber variáveis e concatená-las com SQL
def buildQuery (twl, i):        
    return ("UPDATE content_polluters_tweets_original_pt SET Tweet_limpo_PT = \"" + str(twl)+"\" WHERE TweetID = "+ str(i)) + "; \n "



# Irá processar cada tweet limpo em inglês e passar para português
def processar_tweet(row):
    # Row[7] contêm o texto que você desejo trazudir do tweet
    row_7_content = row[7]
    # Limita o conteúdo a 4500 caracteres
    tweetl = row_7_content[:4500]

    time.sleep(1)
    tweet_limpo_pt = TranslateToPt(tweetl)
#    query = buildQuery(tweet_limpo_pt, row[1])
#    return query
    return row[1], tweet_limpo_pt


######################################PROGRAMA PRINCIPAL#####################################################################
def main():
    while True:
        try:      
            # Criando um objeto de conexão com o banco de dados
            db = pymysql.connect(host = 'localhost', user = 'root', password = 'jef123*', db = 'ime',  autocommit=True)
               
            # Criando objetos cursor
            cursor_tweets = db.cursor()
            cursor_twtlimpo_column = db.cursor()
            
            # Montando SQL statements  
            #sql_tweets = 'SELECT * FROM content_polluters_tweets_original_pt where tweet_limpo_pt is null'
            #sql_tweets = "SELECT * FROM content_polluters_tweets_original_pt where Tweet_limpo_pt COLLATE utf8mb4_general_ci = tweet_limpo and Tweet_limpo is not null and Tweet_limpo not like '' "     
            sql_tweets = "SELECT * FROM content_polluters_tweets_original_pt where tweet_limpo_pt like '' and tweet_limpo not like '' order by TweetID desc"
            # Interação inicial com o banco de dados     
            cursor_tweets.execute(sql_tweets)
            result_tweets = cursor_tweets.fetchall()    
            #Vou criar uma varíavel para armazenar as query´s de update até 100 e depois rodar"
            vCountQuery = 0
    
            # Usando ThreadPoolExecutor para processar os tweets em paralelo
            with ThreadPoolExecutor() as executor:
    #            queries = list(tqdm(executor.map(processar_tweet, result_tweets), total=len(result_tweets)))
    
                for vIdTweet, tweet_limpo_pt in tqdm(executor.map(processar_tweet, result_tweets), total=len(result_tweets)):
                    #print('vIdTweet : ',vIdTweet)
                    query = buildQuery(tweet_limpo_pt, vIdTweet)
                    cursor_twtlimpo_column.execute(query)
                    vCountQuery += 1
                    if vCountQuery == 5:                    
                        db.commit()
                        agora = datetime.datetime.now()
                        print(f"Transação bem-sucedida para os últimos {vCountQuery} registros! - {agora}")
                        vCountQuery = 0
                        
                    #vCountQuery += 1   
            # Finalizar a transação, se houver atualizações pendentes
            if vCountQuery > 0:
                db.commit()            
                
            # Se chegou até aqui sem lançar exceções, sair do loop
            break 

        except Exception as e:
            print("Exceção ocorrida: {}. Reiniciando o processo. ".format(e))

#            print("Exceção ocorrida: {}. Reiniciando o processo. última query {} do IdTweet {} e tweet limpo {}".format(e, query, vIdTweet, tweet_limpo_pt))
            # Rollback in case there is any error
            db.rollback()
            # Esperar um pouco antes de tentar novamente (evitar looping muito rápido em caso de erros frequentes)
            time.sleep(10)            
        finally:   
            db.close()



if __name__=="__main__":
    main()
    
 