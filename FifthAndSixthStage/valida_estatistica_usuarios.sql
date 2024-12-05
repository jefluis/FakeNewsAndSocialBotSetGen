/* Legitimate_Users */
SELECT TweetID, Valence, Arousal, Dominance FROM legitimate_users_tweets_original;
SELECT TweetID, Val, Aro, Dom FROM legitimate_users_tweets_original_pt

REATE TABLE legitimate_usersToPortuguese SELECT * FROM legitimate_users
pdate legitimate_usersToPortuguese set Update_Control = 0
pdate legitimate_usersToPortuguese set Update_Control3 = 0

/* Quantos usuários distintos que tiveram tweets */
SELECT count(distinct UserID) FROM legitimate_users_tweets_original_pt

/* Quantos usuários tem na base original que foi feito o calculo de VAD e Tang e quantos estão 
na base que eu gerei para receber os cálculos com VAD e Tang traduzido*/
select count(*) from legitimate_users where update_control3=1;
select count(*) from legitimate_usersToPortuguese where update_control =1;
select count(*) from legitimate_usersToPortuguese where Update_Control3 =1;

/* Comparo se os valores ficaram diferente, pois no primeiro foi com VAD e Tang em inglês e 
no segundo com VAD e Tang traduzido para portuguess*/
select * from legitimate_users where update_control =1;
select * from legitimate_usersToPortuguese where update_control =1


/*  Content_Polluters */
REATE TABLE Content_PollutersToPortuguese SELECT * FROM Content_Polluters
pdate Content_PollutersToPortuguese set Update_Control = 0;
pdate Content_PollutersToPortuguese set Update_Control3 = 0

/* Quantos usuários tem na base original que foi feito o calculo de VAD e Tang e quantos estão 
na base que eu gerei para receber os cálculos com VAD e Tang traduzido*/
select count(*) from Content_Polluters where update_control =1;
select count(*) from Content_PollutersToPortuguese where update_control =1;
select count(*) from Content_PollutersToPortuguese where update_control3 =1;

/* Comparo se os valores ficaram diferente, pois no primeiro foi com VAD e Tang em inglês e 
no segundo com VAD e Tang traduzido para portuguess*/
select * from Content_Polluters where update_control =1 ;
select * from Content_PollutersToPortuguese where update_control =1 ;


SELECT TweetID, Valence, Arousal, Dominance FROM content_polluters_tweets_original
SELECT TweetID, Val, Aro, Dom FROM content_polluters_tweets_original_pt;

SELECT count(distinct tweetId) FROM content_polluters_tweets_original;
SELECT count(distinct tweetId) FROM content_polluters_tweets_original_pt; 


/* outras verificações*/
SELECT Menor.tweetId as menor_id , menor.userid
FROM content_polluters_tweets as Menor
left join content_polluters_tweets_original_pt as maior on maior.TweetID = menor.TweetID
where maior.tweetId is null
order by menor.userid

SELECT count(distinct menor.userid)
FROM content_polluters_tweets as Menor
left join content_polluters_tweets_original_pt as maior on maior.TweetID = menor.TweetID
where maior.tweetId is null
order by menor.userid

/*TweetOfLabaled*/
SELECT count(*) FROM TweetsOfLabeledNews WHERE Control1=1;
SELECT count(*) FROM TweetsOfLabeledNews WHERE Control2=1;

pdate TweetsOfLabeledNews set Control1=0;
pdate TweetsOfLabeledNews set Control2=0;

SELECT * FROM TweetsOfLabeledNews WHERE Control1=1;

/*users_from_setgen*/
pdate users_from_setgen set Update_Control = 0;
pdate users_from_setgen set update_control3 = 0

select * from users_from_setgenaccounts where Update_Control3 

/* Accounts_Pt */
select * from accounts