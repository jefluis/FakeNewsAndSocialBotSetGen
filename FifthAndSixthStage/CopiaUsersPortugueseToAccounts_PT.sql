/*Cria uma nova tabela accounts e esta irá receber todos os valores de léxicos de 
content_pollutersToPortugues e LegitimateUsersToPortugue, ou seja, são os mesmos 
usuários da base do Samir mas com os resultados de VAD e Tang traduzidos para português*/

CREATE TABLE `accounts_pt` (
  `UserID` int NOT NULL,
  `CreatedAt` datetime NOT NULL,
  `CollectedAt` datetime NOT NULL,
  `NumberOfFollowings` int NOT NULL,
  `NumberOfFollowers` int NOT NULL,
  `NumberOfTweets` int NOT NULL,
  `LengthOfScreenName` int NOT NULL,
  `LenDescrInUseProfile` int NOT NULL,
  `V_media` float NOT NULL,
  `A_media` float NOT NULL,
  `D_media` float NOT NULL,
  `V_1quartil` float NOT NULL,
  `A_1quartil` float NOT NULL,
  `D_1quartil` float NOT NULL,
  `V_mediana` float NOT NULL,
  `A_mediana` float NOT NULL,
  `D_mediana` float NOT NULL,
  `V_3quartil` float NOT NULL,
  `A_3quartil` float NOT NULL,
  `D_3quartil` float NOT NULL,
  `V_desviopadrao` float NOT NULL,
  `A_desviopadrao` float NOT NULL,
  `D_desviopadrao` float NOT NULL,
  `V_amplitude` float NOT NULL,
  `A_amplitude` float NOT NULL,
  `D_amplitude` float NOT NULL,
  `Update_Control` int DEFAULT NULL,
  `Type` varchar(1) NOT NULL DEFAULT 'H',
  `D1_media` float NOT NULL DEFAULT '0',
  `D2_media` float NOT NULL DEFAULT '0',
  `D3_media` float NOT NULL DEFAULT '0',
  `D4_media` float NOT NULL DEFAULT '0',
  `D5_media` float NOT NULL DEFAULT '0',
  `D6_media` float NOT NULL DEFAULT '0',
  `D7_media` float NOT NULL DEFAULT '0',
  `D8_media` float NOT NULL DEFAULT '0',
  `D9_media` float NOT NULL DEFAULT '0',
  `D10_media` float NOT NULL DEFAULT '0',
  `D11_media` float NOT NULL DEFAULT '0',
  `D12_media` float NOT NULL DEFAULT '0',
  `D13_media` float NOT NULL DEFAULT '0',
  `D14_media` float NOT NULL DEFAULT '0',
  `D15_media` float NOT NULL DEFAULT '0',
  `D16_media` float NOT NULL DEFAULT '0',
  `D17_media` float NOT NULL DEFAULT '0',
  `D18_media` float NOT NULL DEFAULT '0',
  `D19_media` float NOT NULL DEFAULT '0',
  `D20_media` float NOT NULL DEFAULT '0',
  `D21_media` float NOT NULL DEFAULT '0',
  `D22_media` float NOT NULL DEFAULT '0',
  `D23_media` float NOT NULL DEFAULT '0',
  `D24_media` float NOT NULL DEFAULT '0',
  `D25_media` float NOT NULL DEFAULT '0',
  `D26_media` float NOT NULL DEFAULT '0',
  `D27_media` float NOT NULL DEFAULT '0',
  `D28_media` float NOT NULL DEFAULT '0',
  `D29_media` float NOT NULL DEFAULT '0',
  `D30_media` float NOT NULL DEFAULT '0',
  `D31_media` float NOT NULL DEFAULT '0',
  `D32_media` float NOT NULL DEFAULT '0',
  `D33_media` float NOT NULL DEFAULT '0',
  `D34_media` float NOT NULL DEFAULT '0',
  `D35_media` float NOT NULL DEFAULT '0',
  `D36_media` float NOT NULL DEFAULT '0',
  `D37_media` float NOT NULL DEFAULT '0',
  `D38_media` float NOT NULL DEFAULT '0',
  `D39_media` float NOT NULL DEFAULT '0',
  `D40_media` float NOT NULL DEFAULT '0',
  `D41_media` float NOT NULL DEFAULT '0',
  `D42_media` float NOT NULL DEFAULT '0',
  `D43_media` float NOT NULL DEFAULT '0',
  `D44_media` float NOT NULL DEFAULT '0',
  `D45_media` float NOT NULL DEFAULT '0',
  `D46_media` float NOT NULL DEFAULT '0',
  `D47_media` float NOT NULL DEFAULT '0',
  `D48_media` float NOT NULL DEFAULT '0',
  `D49_media` float NOT NULL DEFAULT '0',
  `D50_media` float NOT NULL DEFAULT '0',
  `D1_1quartil` float NOT NULL DEFAULT '0',
  `D2_1quartil` float NOT NULL DEFAULT '0',
  `D3_1quartil` float NOT NULL DEFAULT '0',
  `D4_1quartil` float NOT NULL DEFAULT '0',
  `D5_1quartil` float NOT NULL DEFAULT '0',
  `D6_1quartil` float NOT NULL DEFAULT '0',
  `D7_1quartil` float NOT NULL DEFAULT '0',
  `D8_1quartil` float NOT NULL DEFAULT '0',
  `D9_1quartil` float NOT NULL DEFAULT '0',
  `D10_1quartil` float NOT NULL DEFAULT '0',
  `D11_1quartil` float NOT NULL DEFAULT '0',
  `D12_1quartil` float NOT NULL DEFAULT '0',
  `D13_1quartil` float NOT NULL DEFAULT '0',
  `D14_1quartil` float NOT NULL DEFAULT '0',
  `D15_1quartil` float NOT NULL DEFAULT '0',
  `D16_1quartil` float NOT NULL DEFAULT '0',
  `D17_1quartil` float NOT NULL DEFAULT '0',
  `D18_1quartil` float NOT NULL DEFAULT '0',
  `D19_1quartil` float NOT NULL DEFAULT '0',
  `D20_1quartil` float NOT NULL DEFAULT '0',
  `D21_1quartil` float NOT NULL DEFAULT '0',
  `D22_1quartil` float NOT NULL DEFAULT '0',
  `D23_1quartil` float NOT NULL DEFAULT '0',
  `D24_1quartil` float NOT NULL DEFAULT '0',
  `D25_1quartil` float NOT NULL DEFAULT '0',
  `D26_1quartil` float NOT NULL DEFAULT '0',
  `D27_1quartil` float NOT NULL DEFAULT '0',
  `D28_1quartil` float NOT NULL DEFAULT '0',
  `D29_1quartil` float NOT NULL DEFAULT '0',
  `D30_1quartil` float NOT NULL DEFAULT '0',
  `D31_1quartil` float NOT NULL DEFAULT '0',
  `D32_1quartil` float NOT NULL DEFAULT '0',
  `D33_1quartil` float NOT NULL DEFAULT '0',
  `D34_1quartil` float NOT NULL DEFAULT '0',
  `D35_1quartil` float NOT NULL DEFAULT '0',
  `D36_1quartil` float NOT NULL DEFAULT '0',
  `D37_1quartil` float NOT NULL DEFAULT '0',
  `D38_1quartil` float NOT NULL DEFAULT '0',
  `D39_1quartil` float NOT NULL DEFAULT '0',
  `D40_1quartil` float NOT NULL DEFAULT '0',
  `D41_1quartil` float NOT NULL DEFAULT '0',
  `D42_1quartil` float NOT NULL DEFAULT '0',
  `D43_1quartil` float NOT NULL DEFAULT '0',
  `D44_1quartil` float NOT NULL DEFAULT '0',
  `D45_1quartil` float NOT NULL DEFAULT '0',
  `D46_1quartil` float NOT NULL DEFAULT '0',
  `D47_1quartil` float NOT NULL DEFAULT '0',
  `D48_1quartil` float NOT NULL DEFAULT '0',
  `D49_1quartil` float NOT NULL DEFAULT '0',
  `D50_1quartil` float NOT NULL DEFAULT '0',
  `D1_mediana` float NOT NULL DEFAULT '0',
  `D2_mediana` float NOT NULL DEFAULT '0',
  `D3_mediana` float NOT NULL DEFAULT '0',
  `D4_mediana` float NOT NULL DEFAULT '0',
  `D5_mediana` float NOT NULL DEFAULT '0',
  `D6_mediana` float NOT NULL DEFAULT '0',
  `D7_mediana` float NOT NULL DEFAULT '0',
  `D8_mediana` float NOT NULL DEFAULT '0',
  `D9_mediana` float NOT NULL DEFAULT '0',
  `D10_mediana` float NOT NULL DEFAULT '0',
  `D11_mediana` float NOT NULL DEFAULT '0',
  `D12_mediana` float NOT NULL DEFAULT '0',
  `D13_mediana` float NOT NULL DEFAULT '0',
  `D14_mediana` float NOT NULL DEFAULT '0',
  `D15_mediana` float NOT NULL DEFAULT '0',
  `D16_mediana` float NOT NULL DEFAULT '0',
  `D17_mediana` float NOT NULL DEFAULT '0',
  `D18_mediana` float NOT NULL DEFAULT '0',
  `D19_mediana` float NOT NULL DEFAULT '0',
  `D20_mediana` float NOT NULL DEFAULT '0',
  `D21_mediana` float NOT NULL DEFAULT '0',
  `D22_mediana` float NOT NULL DEFAULT '0',
  `D23_mediana` float NOT NULL DEFAULT '0',
  `D24_mediana` float NOT NULL DEFAULT '0',
  `D25_mediana` float NOT NULL DEFAULT '0',
  `D26_mediana` float NOT NULL DEFAULT '0',
  `D27_mediana` float NOT NULL DEFAULT '0',
  `D28_mediana` float NOT NULL DEFAULT '0',
  `D29_mediana` float NOT NULL DEFAULT '0',
  `D30_mediana` float NOT NULL DEFAULT '0',
  `D31_mediana` float NOT NULL DEFAULT '0',
  `D32_mediana` float NOT NULL DEFAULT '0',
  `D33_mediana` float NOT NULL DEFAULT '0',
  `D34_mediana` float NOT NULL DEFAULT '0',
  `D35_mediana` float NOT NULL DEFAULT '0',
  `D36_mediana` float NOT NULL DEFAULT '0',
  `D37_mediana` float NOT NULL DEFAULT '0',
  `D38_mediana` float NOT NULL DEFAULT '0',
  `D39_mediana` float NOT NULL DEFAULT '0',
  `D40_mediana` float NOT NULL DEFAULT '0',
  `D41_mediana` float NOT NULL DEFAULT '0',
  `D42_mediana` float NOT NULL DEFAULT '0',
  `D43_mediana` float NOT NULL DEFAULT '0',
  `D44_mediana` float NOT NULL DEFAULT '0',
  `D45_mediana` float NOT NULL DEFAULT '0',
  `D46_mediana` float NOT NULL DEFAULT '0',
  `D47_mediana` float NOT NULL DEFAULT '0',
  `D48_mediana` float NOT NULL DEFAULT '0',
  `D49_mediana` float NOT NULL DEFAULT '0',
  `D50_mediana` float NOT NULL DEFAULT '0',
  `D1_3quartil` float NOT NULL DEFAULT '0',
  `D2_3quartil` float NOT NULL DEFAULT '0',
  `D3_3quartil` float NOT NULL DEFAULT '0',
  `D4_3quartil` float NOT NULL DEFAULT '0',
  `D5_3quartil` float NOT NULL DEFAULT '0',
  `D6_3quartil` float NOT NULL DEFAULT '0',
  `D7_3quartil` float NOT NULL DEFAULT '0',
  `D8_3quartil` float NOT NULL DEFAULT '0',
  `D9_3quartil` float NOT NULL DEFAULT '0',
  `D10_3quartil` float NOT NULL DEFAULT '0',
  `D11_3quartil` float NOT NULL DEFAULT '0',
  `D12_3quartil` float NOT NULL DEFAULT '0',
  `D13_3quartil` float NOT NULL DEFAULT '0',
  `D14_3quartil` float NOT NULL DEFAULT '0',
  `D15_3quartil` float NOT NULL DEFAULT '0',
  `D16_3quartil` float NOT NULL DEFAULT '0',
  `D17_3quartil` float NOT NULL DEFAULT '0',
  `D18_3quartil` float NOT NULL DEFAULT '0',
  `D19_3quartil` float NOT NULL DEFAULT '0',
  `D20_3quartil` float NOT NULL DEFAULT '0',
  `D21_3quartil` float NOT NULL DEFAULT '0',
  `D22_3quartil` float NOT NULL DEFAULT '0',
  `D23_3quartil` float NOT NULL DEFAULT '0',
  `D24_3quartil` float NOT NULL DEFAULT '0',
  `D25_3quartil` float NOT NULL DEFAULT '0',
  `D26_3quartil` float NOT NULL DEFAULT '0',
  `D27_3quartil` float NOT NULL DEFAULT '0',
  `D28_3quartil` float NOT NULL DEFAULT '0',
  `D29_3quartil` float NOT NULL DEFAULT '0',
  `D30_3quartil` float NOT NULL DEFAULT '0',
  `D31_3quartil` float NOT NULL DEFAULT '0',
  `D32_3quartil` float NOT NULL DEFAULT '0',
  `D33_3quartil` float NOT NULL DEFAULT '0',
  `D34_3quartil` float NOT NULL DEFAULT '0',
  `D35_3quartil` float NOT NULL DEFAULT '0',
  `D36_3quartil` float NOT NULL DEFAULT '0',
  `D37_3quartil` float NOT NULL DEFAULT '0',
  `D38_3quartil` float NOT NULL DEFAULT '0',
  `D39_3quartil` float NOT NULL DEFAULT '0',
  `D40_3quartil` float NOT NULL DEFAULT '0',
  `D41_3quartil` float NOT NULL DEFAULT '0',
  `D42_3quartil` float NOT NULL DEFAULT '0',
  `D43_3quartil` float NOT NULL DEFAULT '0',
  `D44_3quartil` float NOT NULL DEFAULT '0',
  `D45_3quartil` float NOT NULL DEFAULT '0',
  `D46_3quartil` float NOT NULL DEFAULT '0',
  `D47_3quartil` float NOT NULL DEFAULT '0',
  `D48_3quartil` float NOT NULL DEFAULT '0',
  `D49_3quartil` float NOT NULL DEFAULT '0',
  `D50_3quartil` float NOT NULL DEFAULT '0',
  `D1_desviopadrao` float NOT NULL DEFAULT '0',
  `D2_desviopadrao` float NOT NULL DEFAULT '0',
  `D3_desviopadrao` float NOT NULL DEFAULT '0',
  `D4_desviopadrao` float NOT NULL DEFAULT '0',
  `D5_desviopadrao` float NOT NULL DEFAULT '0',
  `D6_desviopadrao` float NOT NULL DEFAULT '0',
  `D7_desviopadrao` float NOT NULL DEFAULT '0',
  `D8_desviopadrao` float NOT NULL DEFAULT '0',
  `D9_desviopadrao` float NOT NULL DEFAULT '0',
  `D10_desviopadrao` float NOT NULL DEFAULT '0',
  `D11_desviopadrao` float NOT NULL DEFAULT '0',
  `D12_desviopadrao` float NOT NULL DEFAULT '0',
  `D13_desviopadrao` float NOT NULL DEFAULT '0',
  `D14_desviopadrao` float NOT NULL DEFAULT '0',
  `D15_desviopadrao` float NOT NULL DEFAULT '0',
  `D16_desviopadrao` float NOT NULL DEFAULT '0',
  `D17_desviopadrao` float NOT NULL DEFAULT '0',
  `D18_desviopadrao` float NOT NULL DEFAULT '0',
  `D19_desviopadrao` float NOT NULL DEFAULT '0',
  `D20_desviopadrao` float NOT NULL DEFAULT '0',
  `D21_desviopadrao` float NOT NULL DEFAULT '0',
  `D22_desviopadrao` float NOT NULL DEFAULT '0',
  `D23_desviopadrao` float NOT NULL DEFAULT '0',
  `D24_desviopadrao` float NOT NULL DEFAULT '0',
  `D25_desviopadrao` float NOT NULL DEFAULT '0',
  `D26_desviopadrao` float NOT NULL DEFAULT '0',
  `D27_desviopadrao` float NOT NULL DEFAULT '0',
  `D28_desviopadrao` float NOT NULL DEFAULT '0',
  `D29_desviopadrao` float NOT NULL DEFAULT '0',
  `D30_desviopadrao` float NOT NULL DEFAULT '0',
  `D31_desviopadrao` float NOT NULL DEFAULT '0',
  `D32_desviopadrao` float NOT NULL DEFAULT '0',
  `D33_desviopadrao` float NOT NULL DEFAULT '0',
  `D34_desviopadrao` float NOT NULL DEFAULT '0',
  `D35_desviopadrao` float NOT NULL DEFAULT '0',
  `D36_desviopadrao` float NOT NULL DEFAULT '0',
  `D37_desviopadrao` float NOT NULL DEFAULT '0',
  `D38_desviopadrao` float NOT NULL DEFAULT '0',
  `D39_desviopadrao` float NOT NULL DEFAULT '0',
  `D40_desviopadrao` float NOT NULL DEFAULT '0',
  `D41_desviopadrao` float NOT NULL DEFAULT '0',
  `D42_desviopadrao` float NOT NULL DEFAULT '0',
  `D43_desviopadrao` float NOT NULL DEFAULT '0',
  `D44_desviopadrao` float NOT NULL DEFAULT '0',
  `D45_desviopadrao` float NOT NULL DEFAULT '0',
  `D46_desviopadrao` float NOT NULL DEFAULT '0',
  `D47_desviopadrao` float NOT NULL DEFAULT '0',
  `D48_desviopadrao` float NOT NULL DEFAULT '0',
  `D49_desviopadrao` float NOT NULL DEFAULT '0',
  `D50_desviopadrao` float NOT NULL DEFAULT '0',
  `D1_amplitude` float NOT NULL DEFAULT '0',
  `D2_amplitude` float NOT NULL DEFAULT '0',
  `D3_amplitude` float NOT NULL DEFAULT '0',
  `D4_amplitude` float NOT NULL DEFAULT '0',
  `D5_amplitude` float NOT NULL DEFAULT '0',
  `D6_amplitude` float NOT NULL DEFAULT '0',
  `D7_amplitude` float NOT NULL DEFAULT '0',
  `D8_amplitude` float NOT NULL DEFAULT '0',
  `D9_amplitude` float NOT NULL DEFAULT '0',
  `D10_amplitude` float NOT NULL DEFAULT '0',
  `D11_amplitude` float NOT NULL DEFAULT '0',
  `D12_amplitude` float NOT NULL DEFAULT '0',
  `D13_amplitude` float NOT NULL DEFAULT '0',
  `D14_amplitude` float NOT NULL DEFAULT '0',
  `D15_amplitude` float NOT NULL DEFAULT '0',
  `D16_amplitude` float NOT NULL DEFAULT '0',
  `D17_amplitude` float NOT NULL DEFAULT '0',
  `D18_amplitude` float NOT NULL DEFAULT '0',
  `D19_amplitude` float NOT NULL DEFAULT '0',
  `D20_amplitude` float NOT NULL DEFAULT '0',
  `D21_amplitude` float NOT NULL DEFAULT '0',
  `D22_amplitude` float NOT NULL DEFAULT '0',
  `D23_amplitude` float NOT NULL DEFAULT '0',
  `D24_amplitude` float NOT NULL DEFAULT '0',
  `D25_amplitude` float NOT NULL DEFAULT '0',
  `D26_amplitude` float NOT NULL DEFAULT '0',
  `D27_amplitude` float NOT NULL DEFAULT '0',
  `D28_amplitude` float NOT NULL DEFAULT '0',
  `D29_amplitude` float NOT NULL DEFAULT '0',
  `D30_amplitude` float NOT NULL DEFAULT '0',
  `D31_amplitude` float NOT NULL DEFAULT '0',
  `D32_amplitude` float NOT NULL DEFAULT '0',
  `D33_amplitude` float NOT NULL DEFAULT '0',
  `D34_amplitude` float NOT NULL DEFAULT '0',
  `D35_amplitude` float NOT NULL DEFAULT '0',
  `D36_amplitude` float NOT NULL DEFAULT '0',
  `D37_amplitude` float NOT NULL DEFAULT '0',
  `D38_amplitude` float NOT NULL DEFAULT '0',
  `D39_amplitude` float NOT NULL DEFAULT '0',
  `D40_amplitude` float NOT NULL DEFAULT '0',
  `D41_amplitude` float NOT NULL DEFAULT '0',
  `D42_amplitude` float NOT NULL DEFAULT '0',
  `D43_amplitude` float NOT NULL DEFAULT '0',
  `D44_amplitude` float NOT NULL DEFAULT '0',
  `D45_amplitude` float NOT NULL DEFAULT '0',
  `D46_amplitude` float NOT NULL DEFAULT '0',
  `D47_amplitude` float NOT NULL DEFAULT '0',
  `D48_amplitude` float NOT NULL DEFAULT '0',
  `D49_amplitude` float NOT NULL DEFAULT '0',
  `D50_amplitude` float NOT NULL DEFAULT '0',
  `Update_Control3` int DEFAULT NULL
  /*,PRIMARY KEY (`UserID`)
  ,UNIQUE KEY `UserID` (`UserID`)*/
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/* Copio para a tabela Accounts_pt os dados de content_polluterstoportuguese*/
INSERT INTO Accounts_pt SELECT * FROM content_polluterstoportuguese;

/* Copio para a tabela Accounts_pt os dados de legitimate_userstoportuguese*/
INSERT INTO Accounts_pt SELECT * FROM legitimate_userstoportuguese;


#Quantidade de registros
SELECT userId, COUNT(userId) AS total FROM Accounts_pt GROUP BY userId HAVING COUNT(userId) > 1;
SELECT COUNT(DISTINCT USERID) FROM Accounts_pt;
SELECT COUNT(*) FROM content_polluterstoportuguese;
SELECT COUNT(DISTINCT USERID) FROM content_polluterstoportuguese;
SELECT COUNT(*) FROM legitimate_userstoportuguese; 
SELECT COUNT(DISTINCT USERID) FROM legitimate_userstoportuguese; 

/* Deleto os duplicados que estão tanto em legitimate_userstoportuguese quanto em content_polluterstoportuguese*/
delete from Accounts_pt where UserId in (14119816,15958265,16413061)

ALTER TABLE `ime`.`accounts_pt` 
ADD PRIMARY KEY (`UserID`),
ADD UNIQUE INDEX `UserID` (`UserID` ASC) VISIBLE;

/* Alterar o campo type H para 0 e type B para 1*/
update accounts_pt set type = 0 where type = 'H'
update accounts_pt set type = 1 where type = 'B'

/* Validações Account_PT*/
Select * from accounts_pt

select count(u.userid) from users_from_setgen as u 
inner join ( select  userid, count(tweetid) as Mensagens 
			from TweetsOfLabeledNews group by UserId having Mensagens > 5) as T2 
            where T2.userid = u.userid and u.v_media > 0


SELECT pt.userid, pt.type, ori.userid, ori.type 
FROM accounts_pt as pt 
left join accounts as ori on pt.userid = ori.userid where pt.type <> 'H'

sql2_accounts = 'SELECT UserID, CreatedAt, NumberOfFollowings, NumberOfFollowers, NumberOfTweets, LengthOfScreenName, LenDescrInUseProfile, Update_Control, Type FROM accounts_pt'
sql3_accounts = 'SELECT UserID, CreatedAt, NumberOfFollowings, NumberOfFollowers, NumberOfTweets, LengthOfScreenName, LenDescrInUseProfile, Update_Control, type, d1_media, d2_media, d3_media, d4_media, d5_media, d6_media, d7_media, d8_media, d9_media, d10_media, d11_media, d12_media, d13_media, d14_media, d15_media, d16_media, d17_media, d18_media, d19_media, d20_media, d21_media, d22_media, d23_media, d24_media, d25_media, d26_media, d27_media, d28_media, d29_media, d30_media, d31_media, d32_media, d33_media, d34_media, d35_media, d36_media, d37_media, d38_media, d39_media, d40_media, d41_media, d42_media, d43_media, d44_media, d45_media, d46_media, d47_media, d48_media, d49_media, d50_media, d1_1quartil, d2_1quartil, d3_1quartil, d4_1quartil, d5_1quartil, d6_1quartil, d7_1quartil, d8_1quartil, d9_1quartil, d10_1quartil, d11_1quartil, d12_1quartil, d13_1quartil, d14_1quartil, d15_1quartil, d16_1quartil, d17_1quartil, d18_1quartil, d19_1quartil, d20_1quartil, d21_1quartil, d22_1quartil, d23_1quartil, d24_1quartil, d25_1quartil, d26_1quartil, d27_1quartil, d28_1quartil, d29_1quartil, d30_1quartil, d31_1quartil, d32_1quartil, d33_1quartil, d34_1quartil, d35_1quartil, d36_1quartil, d37_1quartil, d38_1quartil, d39_1quartil, d40_1quartil, d41_1quartil, d42_1quartil, d43_1quartil, d44_1quartil, d45_1quartil, d46_1quartil, d47_1quartil, d48_1quartil, d49_1quartil, d50_1quartil, d1_mediana, d2_mediana, d3_mediana, d4_mediana, d5_mediana, d6_mediana, d7_mediana, d8_mediana, d9_mediana, d10_mediana, d11_mediana, d12_mediana, d13_mediana, d14_mediana, d15_mediana, d16_mediana, d17_mediana, d18_mediana, d19_mediana, d20_mediana, d21_mediana, d22_mediana, d23_mediana, d24_mediana, d25_mediana, d26_mediana, d27_mediana, d28_mediana, d29_mediana, d30_mediana, d31_mediana, d32_mediana, d33_mediana, d34_mediana, d35_mediana, d36_mediana, d37_mediana, d38_mediana, d39_mediana, d40_mediana, d41_mediana, d42_mediana, d43_mediana, d44_mediana, d45_mediana, d46_mediana, d47_mediana, d48_mediana, d49_mediana, d50_mediana, d1_3quartil, d2_3quartil, d3_3quartil, d4_3quartil, d5_3quartil, d6_3quartil, d7_3quartil, d8_3quartil, d9_3quartil, d10_3quartil, d11_3quartil, d12_3quartil, d13_3quartil, d14_3quartil, d15_3quartil, d16_3quartil, d17_3quartil, d18_3quartil, d19_3quartil, d20_3quartil, d21_3quartil, d22_3quartil, d23_3quartil, d24_3quartil, d25_3quartil, d26_3quartil, d27_3quartil, d28_3quartil, d29_3quartil, d30_3quartil, d31_3quartil, d32_3quartil, d33_3quartil, d34_3quartil, d35_3quartil, d36_3quartil, d37_3quartil, d38_3quartil, d39_3quartil, d40_3quartil, d41_3quartil, d42_3quartil, d43_3quartil, d44_3quartil, d45_3quartil, d46_3quartil, d47_3quartil, d48_3quartil, d49_3quartil, d50_3quartil, d1_desviopadrao, d2_desviopadrao, d3_desviopadrao, d4_desviopadrao, d5_desviopadrao, d6_desviopadrao, d7_desviopadrao, d8_desviopadrao, d9_desviopadrao, d10_desviopadrao, d11_desviopadrao, d12_desviopadrao, d13_desviopadrao, d14_desviopadrao, d15_desviopadrao, d16_desviopadrao, d17_desviopadrao, d18_desviopadrao, d19_desviopadrao, d20_desviopadrao, d21_desviopadrao, d22_desviopadrao, d23_desviopadrao, d24_desviopadrao, d25_desviopadrao, d26_desviopadrao, d27_desviopadrao, d28_desviopadrao, d29_desviopadrao, d30_desviopadrao, d31_desviopadrao, d32_desviopadrao, d33_desviopadrao, d34_desviopadrao, d35_desviopadrao, d36_desviopadrao, d37_desviopadrao, d38_desviopadrao, d39_desviopadrao, d40_desviopadrao, d41_desviopadrao, d42_desviopadrao, d43_desviopadrao, d44_desviopadrao, d45_desviopadrao, d46_desviopadrao, d47_desviopadrao, d48_desviopadrao, d49_desviopadrao, d50_desviopadrao, d1_amplitude, d2_amplitude, d3_amplitude, d4_amplitude, d5_amplitude, d6_amplitude, d7_amplitude, d8_amplitude, d9_amplitude, d10_amplitude, d11_amplitude, d12_amplitude, d13_amplitude, d14_amplitude, d15_amplitude, d16_amplitude, d17_amplitude, d18_amplitude, d19_amplitude, d20_amplitude, d21_amplitude, d22_amplitude, d23_amplitude, d24_amplitude, d25_amplitude, d26_amplitude, d27_amplitude, d28_amplitude, d29_amplitude, d30_amplitude, d31_amplitude, d32_amplitude, d33_amplitude, d34_amplitude, d35_amplitude, d36_amplitude, d37_amplitude, d38_amplitude, d39_amplitude, d40_amplitude, d41_amplitude, d42_amplitude, d43_amplitude, d44_amplitude, d45_amplitude, d46_amplitude, d47_amplitude, d48_amplitude, d49_amplitude, d50_amplitude FROM accounts_pt'


# para treinamento usando somente os dados de Valence e Arousal
sql_SemDominancia = 'SELECT * FROM accounts_pt'

# Query para buscar os dados das contas dos usuários que compartilharam notícias
# Fake e não Fake e que irei rodar o modelo treinado com V A e classificar as contas.
#sql_users_from_setGen = 'select * from users_from_setgen where v_media > 0 limit 500'
sql_users_from_setGen = 'select u.* from users_from_setgen as u inner join ( select  userid, count(tweetid) as Mensagens from TweetsOfLabeledNews group by UserId having Mensagens > 10) as T2 where T2.userid = u.userid and u.v_media > 0'

