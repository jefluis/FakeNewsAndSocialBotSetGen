*** Legitimate Users ***
SELECT count(*) FROM legitimate_users_tweets_original_pt; 
SELECT count(*) FROM legitimate_users_tweets_original
436798
SELECT count(*) FROM legitimate_users_tweets_original_pt where tweet_limpo_pt is not null; 
SELECT count(*) FROM legitimate_users_tweets_original_pt where tweet_limpo is not null ;

SELECT count(*) FROM legitimate_users_tweets_original_pt where tweet_limpo_pt is null;
SELECT count(*) FROM legitimate_users_tweets_original_pt where tweet_limpo is null ;
SELECT count(*) FROM legitimate_users_tweets_original_pt where tweet_limpo_pt is null and tweet_limpo is not null

SELECT count(*) FROM legitimate_users_tweets_original_pt where tweet_limpo_pt like '' ; 
SELECT count(*) FROM legitimate_users_tweets_original_pt where tweet_limpo like '' ;

SELECT count(*) FROM legitimate_users_tweets_original_pt
where tweet_limpo_pt like '' and Tweet_limpo not like ''; 
SELECT tweet, tweet_limpo, tweet_limpo_pt FROM legitimate_users_tweets_original_pt 
where tweet_limpo_pt like '' and Tweet_limpo not like ''; 

select count(*) from legitimate_users_tweets_original_pt 
where Tweet_limpo_pt COLLATE utf8mb4_general_ci like tweet_limpo
and tweet_limpo not like '' ;
select tweet, tweet_limpo, tweet_limpo_pt from legitimate_users_tweets_original_pt 
where Tweet_limpo_pt COLLATE utf8mb4_general_ci like tweet_limpo 
and tweet_limpo not like '' order by TweetID desc;

SELECT count(*) FROM legitimate_users_tweets_original_pt 
where Tweet_limpo_pt COLLATE utf8mb4_general_ci = tweet_limpo 
and tweet_limpo not like '' and tweet_limpo is not null

select tweetid, tweet_limpo, tweet_limpo_pt FROM legitimate_users_tweets_original_pt 
where Tweet_limpo_pt COLLATE utf8mb4_general_ci = tweet_limpo 
and tweet_limpo not like '' and tweet_limpo is not null
   
*** Content Polluters ***
SELECT count(*) FROM content_polluters_tweets_original_pt; 
SELECT count(*) FROM content_polluters_tweets_original;

SELECT count(*) FROM content_polluters_tweets_original_pt where tweet_limpo_pt is  not null; 
SELECT count(*) FROM content_polluters_tweets_original_pt where tweet_limpo_pt like '' ; 
SELECT count(*) FROM content_polluters_tweets_original_pt where tweet_limpo like '' ;

SELECT count(*) FROM content_polluters_tweets_original_pt 
where tweet_limpo_pt like '' and tweet_limpo not like '' order by TweetID desc;
SELECT tweet, tweet_limpo, tweet_limpo_pt FROM content_polluters_tweets_original_pt 
where tweet_limpo_pt like '' and tweet_limpo not like '' order by TweetID desc

SELECT count(*) FROM content_polluters_tweets_original_pt 
where Tweet_limpo_pt COLLATE utf8mb4_general_ci = tweet_limpo 
	and Tweet_limpo is not null and Tweet_limpo not like '';
SELECT tweet, tweet_limpo, tweet_limpo_pt FROM content_polluters_tweets_original_pt 
where Tweet_limpo_pt COLLATE utf8mb4_general_ci = tweet_limpo 
       and Tweet_limpo is not null and Tweet_limpo not like ''

SELECT tweet, tweet_limpo, tweet_limpo_pt  FROM content_polluters_tweets_original_pt 
where Tweet_limpo_pt COLLATE utf8mb4_general_ci <> tweet_limpo

*** VAD ***
select Id_word, Word, word_pt from espaco_emocional_vad 

select count(*) from espaco_emocional_vad where word_pt like word
select Id_word, Word, word_pt from espaco_emocional_vad where  word_pt like word

select count(*)  from espaco_emocional_vad where word_pt is null
select Id_word, Word, word_pt from espaco_emocional_vad where word_pt is null

*** Tang ***
select count(*) from espaco_emocional_tang 
select Id_word, Word, word_pt from espaco_emocional_tang order by Id_word desc

select count(*) from espaco_emocional_tang where word_pt is null and word is not null;
select Id_word, Word, word_pt from espaco_emocional_tang where word_pt is null and word is not null;

select count(*) from espaco_emocional_tang where word_pt not like word; 
select Id_word, Word, word_pt from espaco_emocional_tang where word_pt  like word;

select count(*)  from espaco_emocional_tang where word_pt is not null;
select Id_word, Word, word_pt from espaco_emocional_tang where word_pt is null;

select count(*) from espaco_emocional_tang  where word_pt like word; 
select Id_word, Word, word_pt from espaco_emocional_tang
 where word like word_pt order by id_word desc; 







