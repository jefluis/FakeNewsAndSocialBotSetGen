select count(distinct TweetsOfLabeledNews.userId)
from TweetsOfLabeledNews 
inner join
( 
       select  userid, count(tweetid) as Mensagens 
       from TweetsOfLabeledNews  
       group by UserId 
       having Mensagens > 25) as T2 
where T2.userid = TweetsOfLabeledNews.userid
      
select u.*
from users_from_setgen as u
inner joinlabelednews
( 
       select  userid, count(tweetid) as Mensagens 
       from TweetsOfLabeledNews  
       group by UserId 
       having Mensagens > 25) as T2 
where T2.userid = u.userid and u.v_media > 0


select u.UserID, count(t.TweetID) as QuantTweet 
from users_from_setgen as u 
join TweetsOfLabeledNews as T on t.userid = u.userid 
group by u.UserID

select T.UserId, count(t.TweetID) as QuantTweet 
from TweetsOfLabeledNews as T 
group by t.UserID having QuantTweet > 450

select u.*
from users_from_setgen as u
inner join
( 
       select  userid, count(tweetid) as Mensagens 
       from TweetsOfLabeledNews  
       group by UserId 
       having Mensagens > 25) as T2 
where T2.userid = u.userid and u.v_media > 0
       

