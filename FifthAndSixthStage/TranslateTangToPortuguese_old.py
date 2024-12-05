# -*- coding: utf-8 -*-
"""
Created on October 13 2023

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
    numero = random.randint(1, 9)
    print('Número:  ', numero)
    if numero == 1:
        #Mtranslate  
        try:  
            translated_text = translate(Tweet, 'pt')
        except:
            return Tweet
        return translated_text    

    if numero == 2:        
        #https://pypi.org/project/googletrans/
        translator = Translator()
        translator.raise_Exception = True;
        try:
            translation = translator.translate(Tweet, dest='pt')
        except:
            return Tweet     
       
        return translation.text
    
    if numero == 3:
        #Translators (Bing) - import translators as ts
        try:         
            return ts.translate_text(query_text=Tweet, translator = 'bing', from_language = 'auto', to_language = 'pt')
        except:
            return Tweet
    
    if numero == 4:        
        #Translators (Google) - import translators as ts
        try: 
            return ts.translate_text(query_text=Tweet, translator = 'google', to_language = 'pt')
        except:
            return Tweet    

    if numero == 5:        
        #Translators (baidu) - import translators as ts
        try: 
            return ts.translate_text(query_text=Tweet, translator = 'baidu', to_language = 'pt')
        except:
            return Tweet  
        
    if numero == 6:
        #Translators (papago) - import translators as ts
        try: 
            return ts.translate_text(query_text=Tweet, translator = 'papago', to_language = 'pt')
        except:
            return Tweet  

    if numero == 7:
        #deep_translator (Google Translator)
        try: 
            translated = GoogleTranslator(source='auto', target='pt').translate(Tweet)
            
        except:
            return Tweet  

        return translated

    if numero == 8:
        #deep_translator (My Memory Translator)
        try: 
            translated = MyMemoryTranslator(source='english', target='portuguese').translate(Tweet)
       
        except:
            return Tweet  
        return translated
    
    if numero == 9:    
        #deep_translator (ChatGPT_Translator)
        try: 
            translated = ChatGptTranslator(api_key='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', target='portuguese').translate(Tweet)
        except:
            return Tweet  
        return translated

#Construindo função para receber variáveis e concatená-las com SQL
#def buildQuery (twl, i):        
#    #return ("UPDATE espaco_emocional_tang SET Word_PT = \"" + str(twl)+"\" WHERE Id_Word = "+ str(i)) + "; \n "
#    return ("UPDATE espaco_emocional_tang SET Word_PT = ' " + str(twl)+ " ' WHERE Id_Word = "+ str(i)) + "; \n "


# Irá processar cada tweet limpo em inglês e passar para português
def processar_word(row):
    word_id, word = row
    time.sleep(1)
    word_translate_pt = TranslateToPt(word)
    return word_id, word_translate_pt

######################################PROGRAMA PRINCIPAL#####################################################################

def main():
    # Criando um objeto de conexão com o banco de dados
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'jef123*', db = 'ime',  autocommit=True)
    queryUpdate = "UPDATE espaco_emocional_tang SET Word_PT = %s WHERE Id_Word = %s"

    try:             
        # Criando objetos cursor
        cursor_VAD = db.cursor()
        cursor_Word_PT_column = db.cursor()
        
        # Montando SQL statements  
        sql_VAD = 'select Id_word, Word from espaco_emocional_tang where word  like word_pt or word_pt is null'     
        #sql_VAD = 'select Id_word, Word from espaco_emocional_tang where word like word_pt'     
        
        # Interação inicial com o banco de dados     
        cursor_VAD.execute(sql_VAD)
        result_query = cursor_VAD.fetchall()    
        #Vou criar uma varíavel para armazenar as query´s de update até 100 e depois rodar"
        vCountQuery = 0

        # Usando ThreadPoolExecutor para processar os tweets em paralelo
        with ThreadPoolExecutor() as executor:
#            queries = list(tqdm(executor.map(processar_word, result_query), total=len(result_query)))

            for vIdWord, vWord_pt in tqdm(executor.map(processar_word, result_query), total=len(result_query)):
#            for vIdWord, vWord_pt in tqdm(enumerate(executor.map(processar_word, result_query), 1), total=len(result_query)):
                #query = buildQuery(vWord_pt, vIdWord)
                query = queryUpdate
                values = (vWord_pt, vIdWord)
                cursor_Word_PT_column.execute(query, values)
                vCountQuery += 1
                if vCountQuery == 500:                    
                    db.commit()
                    agora = datetime.datetime.now()
                    print(f"Transação bem-sucedida para os últimos {vCountQuery} registros! - {agora}")
                    vCountQuery = 0
                    
                #vCountQuery += 1   
        # Finalizar a transação, se houver atualizações pendentes
        if vCountQuery > 0:
            db.commit()            
            
    except Exception as e:
        print("Exeception occured:{} e query {} id word {} e palavra traduzida {}".format(e, query, vIdWord, vWord_pt))
        # Rollback in case there is any error
        db.rollback()
    finally:   
        db.close()



if __name__=="__main__":
    main()
    
 