/* Análise Random Forest*/

/*select UserId, prediction_xgboost_vad, prediction_xgboost_twitter_features, prediction_xgboost_tang, prediction_xgboost_vad_tang*/
show variables like "secure_file_priv"


select count(UserId), type, prediction_vad, prediction_tang, prediction_vad_tang, 
prediction_xgboost_vad, prediction_xgboost_tang, prediction_xgboost_vad_tang
from users_from_setgen where prediction_vad is not null
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/predicaonew.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads


select count(*) from users_from_setgen where prediction_vad is not null;

select count(*) from users_from_setgen where prediction_vad =1;
select count(*) from users_from_setgen where prediction_twitter_features =1;
select count(*) from users_from_setgen where prediction_tang =1;
select count(*) from users_from_setgen where prediction_vad_tang =1;

select count(*) from users_from_setgen where prediction_vad =0;
/*select count(*) from users_from_setgen where prediction_twitter_features =0;*/
select count(*) from users_from_setgen where prediction_tang =0;
select count(*) from users_from_setgen where prediction_vad_tang =0;

/*Quantidade total de contas com predição*/
select count(*) from users_from_setgen where prediction_vad is not null;

/*Quantidade total de contas com predições iguais nos quatro modelos*/
select count(*) from users_from_setgen 
where prediction_vad is not null 
and prediction_vad = prediction_twitter_features
and prediction_vad = prediction_tang
and prediction_vad = prediction_vad_tang
;

/*Quantidade total de contas com predições iguais com a predição do VAD*/
select count(*) from users_from_setgen 
where prediction_vad is not null 
and prediction_vad = prediction_twitter_features OR prediction_vad = prediction_tang;

/*Quantidade total de contas com predições iguais com a predição do basic Twitter*/
select count(*) from users_from_setgen 
where prediction_vad is not null 
and prediction_twitter_features = prediction_vad OR prediction_twitter_features = prediction_tang;

/*Quantidade total de contas com predições iguais com a predição do Tang*/
select count(*) from users_from_setgen 
where prediction_vad is not null 
and prediction_tang = prediction_vad OR prediction_twitter_features = prediction_tang;

/*Quantidade total de contas com predições iguais entre a predição do VAD e Tang*/
select count(*) from users_from_setgen 
where prediction_vad = 0
and prediction_tang = prediction_vad 


/* Análise XGBoost*/

/*select UserId, prediction_xgboost_vad, prediction_xgboost_twitter_features, prediction_xgboost_tang, prediction_xgboost_vad_tang*/
select UserId, prediction_xgboost_vad, prediction_xgboost_tang, prediction_xgboost_vad_tang
from users_from_setgen where prediction_xgboost_vad is not null;

select count(*) from users_from_setgen where prediction_xgboost_vad is not null;

select count(*) from users_from_setgen where prediction_xgboost_vad =1;
select count(*) from users_from_setgen where prediction_xgboost_twitter_features =1;
select count(*) from users_from_setgen where prediction_xgboost_tang =1;
select count(*) from users_from_setgen where prediction_xgboost_vad_tang =1;

select count(*) from users_from_setgen where prediction_xgboost_vad =0;
/*select count(*) from users_from_setgen where prediction_xgboost_twitter_features =0;*/
select count(*) from users_from_setgen where prediction_xgboost_tang =0;
select count(*) from users_from_setgen where prediction_xgboost_vad_tang =0;

/*Quantidade total de contas com predição*/
select count(*) from users_from_setgen where prediction_xgboost_vad is not null;

/*Quantidade total de contas com predições iguais nos quatro modelos*/
select count(*) from users_from_setgen 
where prediction_xgboost_vad is not null 
and prediction_xgboost_vad = prediction_xgboost_twitter_features
and prediction_xgboost_vad = prediction_xgboost_tang
and prediction_xgboost_vad = prediction_xgboost_vad_tang
;

/*Quantidade total de contas com predições iguais com a predição do VAD*/
select count(*) from users_from_setgen 
where prediction_xgboost_vad is not null 
and prediction_xgboost_vad = prediction_xgboost_twitter_features OR prediction_xgboost_vad = prediction_xgboost_tang;

/*Quantidade total de contas com predições iguais com a predição do basic Twitter*/
select count(*) from users_from_setgen 
where prediction_xgboost_vad is not null 
and prediction_xgboost_twitter_features = prediction_xgboost_vad OR prediction_xgboost_twitter_features = prediction_xgboost_tang;

/*Quantidade total de contas com predições iguais com a predição do Tang*/
select count(*) from users_from_setgen 
where prediction_xgboost_vad is not null 
and prediction_xgboost_tang = prediction_xgboost_vad OR prediction_xgboost_twitter_features = prediction_xgboost_tang;

/*Quantidade total de contas com predições iguais entre a predição do VAD e Tang*/
select count(*) from users_from_setgen 
where prediction_xgboost_vad = 0
and prediction_xgboost_tang = prediction_xgboost_vad 


select count(*) from accounts_pt where type =1 ;
select count(*) from accounts_pt where type =0 