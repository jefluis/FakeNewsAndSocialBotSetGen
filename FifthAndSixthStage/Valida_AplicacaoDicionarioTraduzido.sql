*** Legitimate Users ***
SELECT count(*) FROM legitimate_users_tweets_original_pt WHERE Control1=0;
SELECT count(*) FROM legitimate_users_tweets_original_pt WHERE Control1=1;
SELECT count(*) FROM legitimate_users_tweets_original_pt WHERE Control2=0;
SELECT count(*) FROM legitimate_users_tweets_original_pt WHERE Control2=1;

SELECT TweetID, Tweet_Limpo_PT,d1, d2, d3, d25, d31, d38, d50  FROM legitimate_users_tweets_original_pt order by tweetId ;
SELECT TweetID, Tweet_Limpo,d1, d2, d3, d25, d31, d38, d50  FROM legitimate_users_tweets_original order by tweetId ;


*** Content_Polluters ***
SELECT count(*) FROM content_polluters_tweets_original_pt WHERE Control1=0;
SELECT count(*) FROM content_polluters_tweets_original_pt WHERE Control1=1;
SELECT count(*) FROM content_polluters_tweets_original_pt WHERE Control2=0;
SELECT count(*) FROM content_polluters_tweets_original_pt WHERE Control2=1;

SELECT TweetID, Tweet_Limpo_PT, d1, d2, d3, d25, d31, d38, d50  FROM content_polluters_tweets_original_pt order by tweetId ;
SELECT TweetID, Tweet_Limpo, d1, d2, d3, d25, d31, d38, d50 FROM content_polluters_tweets_original order by tweetId ;
