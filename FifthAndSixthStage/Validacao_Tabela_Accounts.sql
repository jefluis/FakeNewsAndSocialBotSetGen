#Quantidade de registros
#SELECT count(*) FROM accounts
#SELECT COUNT(DISTINCT USERID) FROM content_polluters 
#SELECT COUNT(DISTINCT USERID) FROM legitimate_users 


#Quantidade de contas que são content_Polluters
#SELECT COUNT(*) FROM accounts join content_polluters on accounts.userid = content_polluters.userid 
#Quantidade de contas que são legitimate_users
#SELECT COUNT(*) FROM accounts join legitimate_users on accounts.userid = legitimate_users.userid 
#Estes dois valores somados deveria ser o mesmo da query SELECT count(*) FROM accounts, se for maior que dizer que há conta tanto legitimate_users quanto content_polluters


#Se aparecer algum registro da query abaixo significa que 
#uma conta está tanto em legitimate_users quanto em content_polluters outra forma de realizar o double check
#SELECT * FROM accounts 
#join content_polluters on accounts.userid = content_polluters.userid 
#join legitimate_users on accounts.userid = legitimate_users.userid 


#6301 e 10836 são content_polluters
#614, 1038, 1437, 2615, 3148

#SELECT * FROM accounts LIMIT 10
#SELECT * FROM accounts join content_polluters on accounts.userid = content_polluters.userid LIMIT 10 
#SELECT * FROM accounts join legitimate_users on accounts.userid = legitimate_users.userid LIMIT 10