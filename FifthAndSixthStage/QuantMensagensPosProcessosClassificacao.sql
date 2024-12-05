/* Quantidade de noticias FakeNews = 1 = 27 para 228 */
SELECT count(distinct T.LabeledNewsId)
from users_from_setgen as U
join tweetsoflabelednews as T on T.userid = u.userid
where T.FakeNews = 1 and U.prediction_vad is not null 

/* Quantidade de noticias FakeNews = 0 =  189 para 496 */
SELECT count(distinct T.LabeledNewsId)
from users_from_setgen as U
join tweetsoflabelednews as T on T.userid = u.userid
where T.FakeNews = 0 and U.prediction_vad is not null 

/* novo em 30/05/2024 */
CREATE TABLE noticias_balanceadas AS
(
SELECT distinct T.LabeledNewsId
from users_from_setgen as U
join tweetsoflabelednews as T on T.userid = u.userid
where T.FakeNews = 1 and U.prediction_vad is not null 
ORDER BY RAND()
LIMIT 220)
UNION
(
SELECT distinct T.LabeledNewsId
from users_from_setgen as U
join tweetsoflabelednews as T on T.userid = u.userid
where T.FakeNews = 0 and U.prediction_vad is not null 
ORDER BY RAND()
LIMIT 220)

select * from noticias_balanceadas

/* Quantidade de noticias FakeNews = 0 =  189 para 496 */
SELECT count(distinct T.LabeledNewsId)
from users_from_setgen as U
join tweetsoflabelednews as T on T.userid = u.userid
where T.FakeNews = 0 and U.prediction_vad is not null 

/* Quantidade de divulgações de noticias FakeNews = 1 = 40675 */
SELECT count(distinct T.tweetID) 
from tweetsoflabelednews as T
join users_from_setgen as U on T.userid = u.userid 
where T.FakeNews = 1 and U.prediction_vad is not null; 

/* Quantidade de divulgações de noticias não FakeNews = 0  = 1928  */
SELECT count(distinct T.tweetID) 
from tweetsoflabelednews as T
join users_from_setgen as U on T.userid = u.userid 
where T.FakeNews = 0 and U.prediction_vad is not null 

/* Quantidade de usuários na fase final = 2141*/
SELECT count(distinct userid) FROM users_from_setgen where prediction_vad is not null

/* Quantidade de usuários de seguidos = 7154643 e seguidores = 63966962*/
SELECT count(userid), sum(numberoffollowings), sum(numberoffollowers) 
from users_from_setgen 
where prediction_vad is not null

/* Quantidade de usuários de seguidos = 7154643 e seguidores = 63966962*/
SELECT count(userid), sum(numberoffollowings), sum(numberoffollowers) 
from users_from_setgen 
where prediction_vad is not null

/* Quantidade de tweet = 42603 e de notícias  e total usuarios 2141 */
SELECT count(distinct T.tweetID) , count(distinct T.LabeledNewsId), count(distinct T.userid) 
from tweetsoflabelednews as T
join users_from_setgen as U on T.userid = u.userid 
where U.prediction_vad is not null 

/* Quantidade de notícias por usuário */
SELECT count(distinct T.LabeledNewsId)
from tweetsoflabelednews as T
join users_from_setgen as U on T.userid = u.userid 
where U.prediction_vad is not null 
group by u.userid 
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/quant_mensagem_por_usu.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

/* Quantidade de usuários por notícias*/
SELECT count(distinct T.userid)
from tweetsoflabelednews as T
join users_from_setgen as U on T.userid = u.userid 
where U.prediction_vad is not null 
group by T.LabeledNewsId
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/quant_usu_por_noticia.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';


/***********   ANÁLISE CONTA BOT E NÃO BOT ************/

/*Quantidade de contas bot = 1366 */
SELECT count(*)
from users_from_setgen as U 
where U.prediction_vad is not null and u.type = 1

/*Quantidade de contas humano = 775 */
SELECT count(*)
from users_from_setgen as U 
where U.prediction_vad is not null and u.type = 0

/* Quantidade de noticias para contas bot =  187 */
SELECT count(distinct T.LabeledNewsId) 
from users_from_setgen as U
join tweetsoflabelednews as T on T.userid = u.userid
join labelednews as L on L.id = T.LabeledNewsID
where U.prediction_vad is not null and u.type = 1;

/* Quantidade de noticias para contas humano =  173 */
SELECT count(distinct T.LabeledNewsId) 
from users_from_setgen as U
join tweetsoflabelednews as T on T.userid = u.userid
join labelednews as L on L.id = T.LabeledNewsID
where U.prediction_vad is not null and u.type = 0;

/* Quantidade de noticias FakeNews = 1 para contas bot = 27 */
SELECT count(distinct T.LabeledNewsId) 
from users_from_setgen as U
join tweetsoflabelednews as T on T.userid = u.userid
join labelednews as L on L.id = T.LabeledNewsID
where T.FakeNews = 1 and U.prediction_vad is not null and u.type = 1;

/* Quantidade de noticias FakeNews = 1 para contas humano = 20 */
SELECT count(distinct T.LabeledNewsId) 
from users_from_setgen as U
join tweetsoflabelednews as T on T.userid = u.userid
join labelednews as L on L.id = T.LabeledNewsID
where T.FakeNews = 1 and U.prediction_vad is not null and u.type = 0

/* Quantidade de noticias FakeNews = 0 para contas bot = 160 */
SELECT count(distinct T.LabeledNewsId)
from users_from_setgen as U
join tweetsoflabelednews as T on T.userid = u.userid
join labelednews as L on L.id = T.LabeledNewsID
where T.FakeNews = 0 and U.prediction_vad is not null and u.type = 1;

/* Quantidade de noticias FakeNews = 0 para contas humano = 153 */
SELECT count(distinct T.LabeledNewsId)
from users_from_setgen as U
join tweetsoflabelednews as T on T.userid = u.userid
join labelednews as L on L.id = T.LabeledNewsID
where T.FakeNews = 0 and U.prediction_vad is not null and u.type = 0;

/* Quantidade de divulgações de noticias FakeNews = 1 por bot = 26077 */
SELECT count(distinct T.tweetID) 
from tweetsoflabelednews as T
join users_from_setgen as U on T.userid = u.userid 
where T.FakeNews = 1 and U.prediction_vad is not null and u.type = 1; 

/* Quantidade de divulgações de noticias FakeNews = 1 por humano = 14598 */
SELECT count(distinct T.tweetID) 
from tweetsoflabelednews as T
join users_from_setgen as U on T.userid = u.userid 
where T.FakeNews = 1 and U.prediction_vad is not null and u.type = 0;

/* Quantidade de divulgações de noticias não FakeNews = 0  por bot = 1108*/
SELECT count(distinct T.tweetID) 
from tweetsoflabelednews as T
join users_from_setgen as U on T.userid = u.userid 
where T.FakeNews = 0 and U.prediction_vad is not null and u.type = 1;

/* Quantidade de divulgações de noticias não FakeNews = 0  por humano = 820 */
SELECT count(distinct T.tweetID) 
from tweetsoflabelednews as T
join users_from_setgen as U on T.userid = u.userid 
where T.FakeNews = 0 and U.prediction_vad is not null and u.type = 0

gfgdfsfdggfdsg

/* Quantidade de usuários de seguidos = 5575929  e seguidores = 22088166 para bot */
SELECT count(userid), sum(numberoffollowings), sum(numberoffollowers) 
from users_from_setgen 
where prediction_vad is not null and type = 1;

/* Quantidade de usuários de seguidos = 1578714 e seguidores = 41878796 para humano*/
SELECT count(userid), sum(numberoffollowings), sum(numberoffollowers) 
from users_from_setgen 
where prediction_vad is not null and type = 0

/* Quantidade de tweet =  e de notícias  e total usuarios  para bot */
SELECT count(distinct T.tweetID) , count(distinct T.LabeledNewsId), count(distinct T.userid) 
from tweetsoflabelednews as T
join users_from_setgen as U on T.userid = u.userid 
where U.prediction_vad is not null and type = 1

/* Quantidade de tweet =  e de notícias  e total usuarios  para humano */
SELECT count(distinct T.tweetID) , count(distinct T.LabeledNewsId), count(distinct T.userid) 
from tweetsoflabelednews as T
join users_from_setgen as U on T.userid = u.userid 
where U.prediction_vad is not null and type = 0

/* Quantidade de notícias por usuário bot */
SELECT count(distinct T.LabeledNewsId)
from tweetsoflabelednews as T
join users_from_setgen as U on T.userid = u.userid 
where U.prediction_vad is not null and u.type = 1
group by u.userid 
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/quant_mensagem_por_usu_bot.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

/* Quantidade de notícias por usuário humano */
SELECT count(distinct T.LabeledNewsId)
from tweetsoflabelednews as T
join users_from_setgen as U on T.userid = u.userid 
where U.prediction_vad is not null and u.type = 0
group by u.userid 
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/quant_mensagem_por_usu_hum.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

/* Quantidade de usuários bot por notícias */
SELECT count(distinct T.userid)
from tweetsoflabelednews as T
join users_from_setgen as U on T.userid = u.userid 
where U.prediction_vad is not null and u.type = 1
group by T.LabeledNewsId 
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/quant_usu_bot_por_noticia_N.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

/* Quantidade de usuários Humano por notícias */
SELECT count(distinct T.userid)
from tweetsoflabelednews as T
join users_from_setgen as U on T.userid = u.userid 
where U.prediction_vad is not null and u.type = 0
group by T.LabeledNewsId 
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/quant_usu_humano_por_noticia_N.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

/**/
SELECT * FROM labelednews;
SELECT * FROM tweetsoflabelednews
GROUP BY LabeledNewsId;
SELECT * FROM users_from_setgen

    SELECT u.UserID, CreatedAt, NumberOfFollowings, NumberOfFollowers, NumberOfTweets, 
            LengthOfScreenName, LenDescrInUseProf as LenDescrInUseProfile, type, 
            V_media, A_media, D_media, 
            V_1quartil ,  A_1quartil ,  D_1quartil , 
            V_mediana ,  A_mediana ,  D_mediana , 
            V_3quartil ,  A_3quartil ,  D_3quartil , 
            V_desviopadrao ,  A_desviopadrao ,  D_desviopadrao , 
            V_amplitude ,  A_amplitude ,  D_amplitude,
            d1_media, d2_media, d3_media, d4_media, d5_media, d6_media, d7_media, d8_media, d9_media, d10_media, d11_media, d12_media, d13_media, d14_media, d15_media, d16_media, d17_media, d18_media, d19_media, d20_media, d21_media, d22_media, d23_media, d24_media, d25_media, d26_media, d27_media, d28_media, d29_media, d30_media, d31_media, d32_media, d33_media, d34_media, d35_media, d36_media, d37_media, d38_media, d39_media, d40_media, d41_media, d42_media, d43_media, d44_media, d45_media, d46_media, d47_media, d48_media, d49_media, d50_media, 
            d1_1quartil, d2_1quartil, d3_1quartil, d4_1quartil, d5_1quartil, d6_1quartil, d7_1quartil, d8_1quartil, d9_1quartil, d10_1quartil, d11_1quartil, d12_1quartil, d13_1quartil, d14_1quartil, d15_1quartil, d16_1quartil, d17_1quartil, d18_1quartil, d19_1quartil, d20_1quartil, d21_1quartil, d22_1quartil, d23_1quartil, d24_1quartil, d25_1quartil, d26_1quartil, d27_1quartil, d28_1quartil, d29_1quartil, d30_1quartil, d31_1quartil, d32_1quartil, d33_1quartil, d34_1quartil, d35_1quartil, d36_1quartil, d37_1quartil, d38_1quartil, d39_1quartil, d40_1quartil, d41_1quartil, d42_1quartil, d43_1quartil, d44_1quartil, d45_1quartil, d46_1quartil, d47_1quartil, d48_1quartil, d49_1quartil, d50_1quartil, 
            d1_mediana, d2_mediana, d3_mediana, d4_mediana, d5_mediana, d6_mediana, d7_mediana, d8_mediana, d9_mediana, d10_mediana, d11_mediana, d12_mediana, d13_mediana, d14_mediana, d15_mediana, d16_mediana, d17_mediana, d18_mediana, d19_mediana, d20_mediana, d21_mediana, d22_mediana, d23_mediana, d24_mediana, d25_mediana, d26_mediana, d27_mediana, d28_mediana, d29_mediana, d30_mediana, d31_mediana, d32_mediana, d33_mediana, d34_mediana, d35_mediana, d36_mediana, d37_mediana, d38_mediana, d39_mediana, d40_mediana, d41_mediana, d42_mediana, d43_mediana, d44_mediana, d45_mediana, d46_mediana, d47_mediana, d48_mediana, d49_mediana, d50_mediana, 
            d1_3quartil, d2_3quartil, d3_3quartil, d4_3quartil, d5_3quartil, d6_3quartil, d7_3quartil, d8_3quartil, d9_3quartil, d10_3quartil, d11_3quartil, d12_3quartil, d13_3quartil, d14_3quartil, d15_3quartil, d16_3quartil, d17_3quartil, d18_3quartil, d19_3quartil, d20_3quartil, d21_3quartil, d22_3quartil, d23_3quartil, d24_3quartil, d25_3quartil, d26_3quartil, d27_3quartil, d28_3quartil, d29_3quartil, d30_3quartil, d31_3quartil, d32_3quartil, d33_3quartil, d34_3quartil, d35_3quartil, d36_3quartil, d37_3quartil, d38_3quartil, d39_3quartil, d40_3quartil, d41_3quartil, d42_3quartil, d43_3quartil, d44_3quartil, d45_3quartil, d46_3quartil, d47_3quartil, d48_3quartil, d49_3quartil, d50_3quartil, 
            d1_desviopadrao, d2_desviopadrao, d3_desviopadrao, d4_desviopadrao, d5_desviopadrao, d6_desviopadrao, d7_desviopadrao, d8_desviopadrao, d9_desviopadrao, d10_desviopadrao, d11_desviopadrao, d12_desviopadrao, d13_desviopadrao, d14_desviopadrao, d15_desviopadrao, d16_desviopadrao, d17_desviopadrao, d18_desviopadrao, d19_desviopadrao, d20_desviopadrao, d21_desviopadrao, d22_desviopadrao, d23_desviopadrao, d24_desviopadrao, d25_desviopadrao, d26_desviopadrao, d27_desviopadrao, d28_desviopadrao, d29_desviopadrao, d30_desviopadrao, d31_desviopadrao, d32_desviopadrao, d33_desviopadrao, d34_desviopadrao, d35_desviopadrao, d36_desviopadrao, d37_desviopadrao, d38_desviopadrao, d39_desviopadrao, d40_desviopadrao, d41_desviopadrao, d42_desviopadrao, d43_desviopadrao, d44_desviopadrao, d45_desviopadrao, d46_desviopadrao, d47_desviopadrao, d48_desviopadrao, d49_desviopadrao, d50_desviopadrao, 
            d1_amplitude, d2_amplitude, d3_amplitude, d4_amplitude, d5_amplitude, d6_amplitude, d7_amplitude, d8_amplitude, d9_amplitude, d10_amplitude, d11_amplitude, d12_amplitude, d13_amplitude, d14_amplitude, d15_amplitude, d16_amplitude, d17_amplitude, d18_amplitude, d19_amplitude, d20_amplitude, d21_amplitude, d22_amplitude, d23_amplitude, d24_amplitude, d25_amplitude, d26_amplitude, d27_amplitude, d28_amplitude, d29_amplitude, d30_amplitude, d31_amplitude, d32_amplitude, d33_amplitude, d34_amplitude, d35_amplitude, d36_amplitude, d37_amplitude, d38_amplitude, d39_amplitude, d40_amplitude, d41_amplitude, d42_amplitude, d43_amplitude, d44_amplitude, d45_amplitude, d46_amplitude, d47_amplitude, d48_amplitude, d49_amplitude, d50_amplitude 
    FROM users_from_setgen AS u
    INNER JOIN (
        SELECT userid, COUNT(tweetid) AS Mensagens
        FROM TweetsOfLabeledNews
        GROUP BY UserId
        HAVING Mensagens > 10
    ) AS T2
    WHERE T2.userid = u.userid AND u.v_media > 0
    
select count(final.userid) from(
SELECT u.UserID, CreatedAt, NumberOfFollowings, NumberOfFollowers, NumberOfTweets, 
            LengthOfScreenName, LenDescrInUseProf as LenDescrInUseProfile, type, 
            V_media, A_media, D_media, 
            V_1quartil ,  A_1quartil ,  D_1quartil , 
            V_mediana ,  A_mediana ,  D_mediana , 
            V_3quartil ,  A_3quartil ,  D_3quartil , 
            V_desviopadrao ,  A_desviopadrao ,  D_desviopadrao , 
            V_amplitude ,  A_amplitude ,  D_amplitude,
            d1_media, d2_media, d3_media, d4_media, d5_media, d6_media, d7_media, d8_media, d9_media, d10_media, d11_media, d12_media, d13_media, d14_media, d15_media, d16_media, d17_media, d18_media, d19_media, d20_media, d21_media, d22_media, d23_media, d24_media, d25_media, d26_media, d27_media, d28_media, d29_media, d30_media, d31_media, d32_media, d33_media, d34_media, d35_media, d36_media, d37_media, d38_media, d39_media, d40_media, d41_media, d42_media, d43_media, d44_media, d45_media, d46_media, d47_media, d48_media, d49_media, d50_media, 
            d1_1quartil, d2_1quartil, d3_1quartil, d4_1quartil, d5_1quartil, d6_1quartil, d7_1quartil, d8_1quartil, d9_1quartil, d10_1quartil, d11_1quartil, d12_1quartil, d13_1quartil, d14_1quartil, d15_1quartil, d16_1quartil, d17_1quartil, d18_1quartil, d19_1quartil, d20_1quartil, d21_1quartil, d22_1quartil, d23_1quartil, d24_1quartil, d25_1quartil, d26_1quartil, d27_1quartil, d28_1quartil, d29_1quartil, d30_1quartil, d31_1quartil, d32_1quartil, d33_1quartil, d34_1quartil, d35_1quartil, d36_1quartil, d37_1quartil, d38_1quartil, d39_1quartil, d40_1quartil, d41_1quartil, d42_1quartil, d43_1quartil, d44_1quartil, d45_1quartil, d46_1quartil, d47_1quartil, d48_1quartil, d49_1quartil, d50_1quartil, 
            d1_mediana, d2_mediana, d3_mediana, d4_mediana, d5_mediana, d6_mediana, d7_mediana, d8_mediana, d9_mediana, d10_mediana, d11_mediana, d12_mediana, d13_mediana, d14_mediana, d15_mediana, d16_mediana, d17_mediana, d18_mediana, d19_mediana, d20_mediana, d21_mediana, d22_mediana, d23_mediana, d24_mediana, d25_mediana, d26_mediana, d27_mediana, d28_mediana, d29_mediana, d30_mediana, d31_mediana, d32_mediana, d33_mediana, d34_mediana, d35_mediana, d36_mediana, d37_mediana, d38_mediana, d39_mediana, d40_mediana, d41_mediana, d42_mediana, d43_mediana, d44_mediana, d45_mediana, d46_mediana, d47_mediana, d48_mediana, d49_mediana, d50_mediana, 
            d1_3quartil, d2_3quartil, d3_3quartil, d4_3quartil, d5_3quartil, d6_3quartil, d7_3quartil, d8_3quartil, d9_3quartil, d10_3quartil, d11_3quartil, d12_3quartil, d13_3quartil, d14_3quartil, d15_3quartil, d16_3quartil, d17_3quartil, d18_3quartil, d19_3quartil, d20_3quartil, d21_3quartil, d22_3quartil, d23_3quartil, d24_3quartil, d25_3quartil, d26_3quartil, d27_3quartil, d28_3quartil, d29_3quartil, d30_3quartil, d31_3quartil, d32_3quartil, d33_3quartil, d34_3quartil, d35_3quartil, d36_3quartil, d37_3quartil, d38_3quartil, d39_3quartil, d40_3quartil, d41_3quartil, d42_3quartil, d43_3quartil, d44_3quartil, d45_3quartil, d46_3quartil, d47_3quartil, d48_3quartil, d49_3quartil, d50_3quartil, 
            d1_desviopadrao, d2_desviopadrao, d3_desviopadrao, d4_desviopadrao, d5_desviopadrao, d6_desviopadrao, d7_desviopadrao, d8_desviopadrao, d9_desviopadrao, d10_desviopadrao, d11_desviopadrao, d12_desviopadrao, d13_desviopadrao, d14_desviopadrao, d15_desviopadrao, d16_desviopadrao, d17_desviopadrao, d18_desviopadrao, d19_desviopadrao, d20_desviopadrao, d21_desviopadrao, d22_desviopadrao, d23_desviopadrao, d24_desviopadrao, d25_desviopadrao, d26_desviopadrao, d27_desviopadrao, d28_desviopadrao, d29_desviopadrao, d30_desviopadrao, d31_desviopadrao, d32_desviopadrao, d33_desviopadrao, d34_desviopadrao, d35_desviopadrao, d36_desviopadrao, d37_desviopadrao, d38_desviopadrao, d39_desviopadrao, d40_desviopadrao, d41_desviopadrao, d42_desviopadrao, d43_desviopadrao, d44_desviopadrao, d45_desviopadrao, d46_desviopadrao, d47_desviopadrao, d48_desviopadrao, d49_desviopadrao, d50_desviopadrao, 
            d1_amplitude, d2_amplitude, d3_amplitude, d4_amplitude, d5_amplitude, d6_amplitude, d7_amplitude, d8_amplitude, d9_amplitude, d10_amplitude, d11_amplitude, d12_amplitude, d13_amplitude, d14_amplitude, d15_amplitude, d16_amplitude, d17_amplitude, d18_amplitude, d19_amplitude, d20_amplitude, d21_amplitude, d22_amplitude, d23_amplitude, d24_amplitude, d25_amplitude, d26_amplitude, d27_amplitude, d28_amplitude, d29_amplitude, d30_amplitude, d31_amplitude, d32_amplitude, d33_amplitude, d34_amplitude, d35_amplitude, d36_amplitude, d37_amplitude, d38_amplitude, d39_amplitude, d40_amplitude, d41_amplitude, d42_amplitude, d43_amplitude, d44_amplitude, d45_amplitude, d46_amplitude, d47_amplitude, d48_amplitude, d49_amplitude, d50_amplitude 
    FROM users_from_setgen AS u
    INNER JOIN (
        SELECT userid, COUNT(tweetid) AS Mensagens
        FROM TweetsOfLabeledNews
        GROUP BY UserId
        HAVING Mensagens > 10
    ) AS T2
    WHERE T2.userid = u.userid AND u.v_media > 0) as final
    
***********************************************************************


***********************************************************
TOTAL DE NOTÍCIAS ROTULADAS = 2959  
TOTAL DE NOTÍCIAS ROTULADAS = FALSO = 1343  
TOTAL DE NOTÍCIAS ROTULADAS = VERDADEIRO = 1562 

select COUNT(*) from labelednews WHERE alternativename LIKE 'FAL%';
select COUNT(*) from labelednews WHERE alternativename LIKE "VERDADE%"

***********************************************************
TOTAL DE TWEETS DE NOTICIAS ROTULADAS = 221089
TOTAL DE TWEETS DE NOTICIAS ROTULADA = FALSO = 210180
TOTAL DE TWEETS DE NOTICIAS ROTULADA = VERDADEIRO = 10909

SELECT COUNT(*) FROM tweetsoflabelednews WHERE FakeNews = 1;
SELECT COUNT(*) FROM tweetsoflabelednews WHERE FakeNews = 0

***********************************************************
TOTAL DE NOTÍCIAS ROTULADAS QUE TIVERAM TWEETS = 275
TOTAL DE NOTÍCIAS ROTULADAS QUE TIVERAM TWEETS = FALSO = 53
TOTAL DE NOTÍCIAS ROTULADAS QUE TIVERAM TWEETS = VERDADEIRO = 222

SELECT count(DISTINCT LabeledNewsId) FROM tweetsoflabelednews WHERE FakeNews = 1;
SELECT count(DISTINCT LabeledNewsId) FROM tweetsoflabelednews WHERE FakeNews = 0


***********************************************************
SELECT 
    t.labelednewsId, 
    COUNT(t.TweetID) AS TweetCount, 
    SUM(t.retweet_count) AS ReTweetCount, 
    SUM(t.favorite_count) AS favorite_count, 
    l.alternativeName,
    COUNT(u.type) AS total_users,    
    SUM(CASE WHEN u.type = 1 THEN 1 ELSE 0 END) AS total_users_type_1,
    SUM(CASE WHEN u.type = 0 THEN 1 ELSE 0 END) AS total_users_type_0,
    CASE WHEN SUM(CASE WHEN u.type = 1 THEN 1 ELSE 0 END) > 
              SUM(CASE WHEN u.type = 0 THEN 1 ELSE 0 END) THEN 1 ELSE 0 END AS BOT
FROM  
    tweetsoflabelednews AS t 
JOIN 
    users_from_setgen AS u ON u.userid = t.userid
JOIN
    labelednews AS l ON t.labelednewsId = l.id
WHERE 
   u.type <> 'H'
GROUP BY 
    t.labelednewsId,  l.alternativeName;
    
    



select count(*) from tweetsoflabelednews
select * from  labelednews
