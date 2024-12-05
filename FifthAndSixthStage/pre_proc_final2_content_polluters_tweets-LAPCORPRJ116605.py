# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 23:38:25 2020

@author: Samir

Updated on December 2022
@author: Jeferson Luis Gonçalves
"""

import pymysql
import re
import nltk
from contractions import CONTRACTION_MAP
from nltk.corpus import wordnet
from tqdm import tqdm

# Jeferson - Begin
from sqlalchemy import create_engine
# Jeferson - End

###########################################################################################################
#APROVADA - Carregar Lista de StopWords
stopWords =[]
sw = open('stopwords.txt', 'r')
for line in sw:
    line2 = line.strip()
    stopWords.append(line2.lower())
# Os termos 'at_user', 'rt' e 'url' foram adicionados manualmente no arquivo stopwords.txt
###########################################################################################################
#APROVADA
def remove_whitespace(tweet):
    "Remove espaços brancos adicionais"
    tweet = re.sub('[\s]+', ' ', tweet)
    return tweet
#APROVADA
def removeUrls(tweet):
    "Substitui os conjuntos www.* e http* por URL, que serão posteriormente removidos pelo StopWords, já que URL/RT/AT_USER serão incluídas como stopwords"
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+) | (http?://[^\s]+))',' URL',tweet)
    return tweet
#APROVADA
def removeUsername(tweet):
    "Transforma em minúsculas e substitui os conjuntos @*** por AT_USER, que serão posteriormente removidos pelo StopWords, já que URL/RT/AT_USER serão incluídas como stopwords"
    tweet = tweet.lower()
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    return tweet
#APROVADA
def removeHashtags(tweet):
    "Substitui os conjuntos #*** por RT"
    tweet = re.sub('#[^\s]+', 'RT', tweet)
    return tweet
#APROVADA
def remove_special_characters(sentence, keep_apostrophes=False):
    sentence = sentence.strip()
    if keep_apostrophes:
        PATTERN = r'[?|$|&|*|%|@|(|)|~|^|<|>]' # add other characters here to remove them
        filtered_sentence = re.sub(PATTERN, r'', sentence)
    else:
        PATTERN = r'[^a-zA-Z ]' # only extract alpha-numeric characters
        filtered_sentence = re.sub(PATTERN, r'', sentence)
    return filtered_sentence
#APROVADA
def expand_contractions(text, contraction_mapping):
    contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())), flags=re.IGNORECASE|re.DOTALL)
    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = contraction_mapping.get(match)\
                                if contraction_mapping.get(match)\
                                else contraction_mapping.get(match.lower())
        #print(type(expanded_contraction))
        expanded_contraction = first_char+expanded_contraction[1:]
        #print(type(expanded_contraction))
        return expanded_contraction
    expanded_text = contractions_pattern.sub(expand_match, text)
    expanded_text = re.sub("'", "", expanded_text)
    return expanded_text
#APROVADA
def remove_repeated_characters(tokens):
    repeat_pattern = re.compile(r'(\w*)(\w)\2(\w*)')
    match_substitution = r'\1\2\3'
    def replace(old_word):
        if wordnet.synsets(old_word):
            return old_word
        new_word = repeat_pattern.sub(match_substitution, old_word)
        return replace(new_word) if new_word != old_word else new_word
    correct_tokens = [replace(word) for word in tokens]
    return correct_tokens
#APROVADA
def remove_non_ascii(txt):
    return ''.join([word for word in txt if ord(word) < 128])
#APROVADA
def remove_stopWords(tweet):
    tweet_stopWordless = []   
    words = tokenize(str(tweet))
    for w in words:         
        w = w.strip('\'"?,.')
        w = w.lower()
        #print(w)
        # check if it consists of only words
        val = w.isalpha() 
        if (w in stopWords or val is False):
            continue
        else:
            tweet_stopWordless.append(w.lower())    
    cleaned_tweet = ' '.join(tweet_stopWordless) # ajunta valores csv de uma lista separados por espaço
    tweet_tokens = tokenize(cleaned_tweet)
    #print (tweet_tokens)
    total_cleaned_tweet = remove_repeated_characters(tweet_tokens)
    #print(total_cleaned_tweet)  
    #print(len(total_cleaned_tweet))       
    total_cleaned_tweet = ' '.join(total_cleaned_tweet)
    #print('Tweet Limpo = ', total_cleaned_tweet) #persistir como tweet_limpo
    return total_cleaned_tweet #pegar só texto e espaço, sem formato de lista
#APROVADA
def tokenize(Tweet):    
    default_wt = nltk.word_tokenize
    words = default_wt(Tweet)
    return words
################################################################
#FUNÇÃO PRINCIPAL
def limpeza (twt):
    #for tweet in Tweets:
        
        #print('******************************')
        twtl = remove_whitespace(twt)
        twtl = expand_contractions(twtl, CONTRACTION_MAP)    
        twtl = removeUsername(twtl)
        twtl = removeHashtags(twtl)  
        twtl = removeUrls(twtl)
        twtl = remove_special_characters(twtl)
        twtl = remove_stopWords(twtl) # COM e SEM Não esquecer!!!
        return (twtl)
######################################PROGRAMA PRINCIPAL#####################################################################

# Jeferson - Begin

# Criando um objeto de conexão com o banco de dados
#db = pymysql.connect(host = 'localhost', user = 'root', password = 'ime@123', db = 'sbseg',  autocommit=True)

#Estrutura 'mysql+pymysql://user:password@ip/schema'
#db = 'mysql+pymysql://root:jef123*@35.231.234.95/ime'
#conn = create_engine(db) or above
db = pymysql.connect(host = 'localhost', user = 'root', password = 'jef123*', db = 'ime',  autocommit=True)

# Jeferson - End


try:
    # Criando objetos cursor
    #cursor_espaco_emocional = db.cursor()
    
    
    cursor_content_polluters_tweets = db.cursor()
    cursor_twtlimpo_column = db.cursor()
    
    
    # Montando SQL statements 
    #sql_espaco_emocional = 'SELECT Id_Word, Word, V_Mean_Sum, A_Mean_Sum, D_Mean_Sum FROM espaco_emocional'    
    sql_teste_tweets = 'SELECT * FROM content_polluters_tweets_original'
      
    #Construindo função para receber variáveis e concatená-las com SQL
    def buildQuery (twl, i):   
        return ("UPDATE content_polluters_tweets_original SET Tweet_limpo = '"+ str(twl)+"' WHERE TweetID = "+ str(i))
        #return ("UPDATE legitimate_users_tweets SET Valence = "+ str(w)+", Arousal = "+ str(x)+", Dominance = "+ str(y)+" WHERE TweetID = "+ str(z))
        
    # Interação inicial com o banco de dados     
    cursor_content_polluters_tweets.execute(sql_teste_tweets)
    result_tweets = cursor_content_polluters_tweets.fetchall()    
   
    # Percorrer cada conjunto
    ##for row in result_tweets:
    for row in tqdm(result_tweets):
        # Split de cada tweet em palavras      
        
        #n = n + 1
        user = row[0]
        twid = row[1]
        tweet = row[2]
        when = row[3]
        #valence = row[4]
        #arousal = row[5]
        #dominance = row[6]       
        tweetl = row[7] # coluna criada/usada para persistir        
        #ID = row[5]
        #print ('TWEET ANALISADO ',n,': ',row[2])
        tweet_limpo = limpeza (tweet)
        #print('---------------------------------------')
        #print('TWEET LIMPO =',tweet_limpo)
        #print('#######################################')
        # Interação com o banco de dados (persistir tweet limpo)
        cursor_twtlimpo_column.execute(buildQuery(tweet_limpo, row[1])) 
                     
    #marcacao
        
except Exception as e:
    print("Exeception occured:{}".format(e))
    # Rollback in case there is any error
    db.rollback()
finally:   
    db.close()


"""
if __name__=="__main__":
    main()
"""



    


