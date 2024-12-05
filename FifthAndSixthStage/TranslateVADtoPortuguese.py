# -*- coding: utf-8 -*-
"""
Created on October 11 2023

@author: Jeferson Luis Gonçalves
"""

import pymysql
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from mtranslate import translate
from googletrans import Translator
import datetime
import time


#Traduzir para português
def TranslateToPt(Tweet):  
    #Mtranslate  
    try:  
        translated_text = translate(Tweet, 'pt')
    except:
        return Tweet
    return translated_text
        
 #==============================================================================
 #    #https://pypi.org/project/googletrans/
 #    translator = Translator()
 #    translator.raise_Exception = True;
 #    try:
 #        translation = translator.translate(Tweet, dest='pt')
 #    except:
 #        return Tweet     
 # 
 #    return translation.text
 #==============================================================================

#Construindo função para receber variáveis e concatená-las com SQL
def buildQuery (twl, i):        
#    return ("UPDATE espaco_emocional_vad SET Word_PT = \" " + str(twl)+" \" WHERE Id_Word = "+ str(i)) + "; \n "
    return ("UPDATE espaco_emocional_vad SET Word_PT = ' " + str(twl)+" ' WHERE Id_Word = "+ str(i)) + "; \n "



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
   
    try:             
        # Criando objetos cursor
        cursor_VAD = db.cursor()
        cursor_Word_PT_column = db.cursor()
        
        # Montando SQL statements  
        #sql_VAD = 'select Id_word, Word from espaco_emocional_vad where word_pt is null'     
        sql_VAD = 'select Id_word, Word from espaco_emocional_vad where word like word_pt'     
        
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
                query = buildQuery(vWord_pt, vIdWord)
                cursor_Word_PT_column.execute(query)
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
    
 