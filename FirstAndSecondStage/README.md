
## Overview  

This code was developed to collect news from reliable sources and associate it with their respective disclosures on social media.

## Imput parameters
The initial configuration for the execution of these two initial stages of FakeNewsSetGen must be carried out at the beginning of the main.py file, through the alteration of the input parameters. An example of configuring these parameters is shown below:
	**agencies - It is intended to include URLs of the spaces used for the dissemination of news feeds by fact-checking agencies.
		   E.g.: ["https://checamos.afp.com/rss/1558/rss.xml","https://aosfatos.org/noticias/feed/", "https://piaui.folha.uol.com.br/lupa/feed/"]
	**virtualMedias - As well as checking agencies, such as renowned virtual media also made news available via RSS feed.
		   	E.g.: ["https://g1.globo.com/rss/g1/tecnologia/", "https://g1.globo.com/rss/g1/educacao/", "https://g1.globo.com/rss/g1/economia/","https://noticias.r7.com/feed.xml"]
	**toprow** = ['id','URL', 'Author', 'datePublished', 'claimReviewed', 'reviewBody', 'title', 'ratingValue', 'bestRating', 'alternativeName']
	**newStopWords** - This parameter must contain, if any, the markers inserted by the checking agencies in the news text. The insertion of these markers in this parameter is essential, as the process removes these words from the set that will compose the social media query.
			E.g.:['#Verificamos:','Checamos','Agência','Lupa','Pública','Aos','Fatos','Fake','FAKE','fake','g1']
	**language** - This parameter must be edited with the language of the news so that the removal of stop words, from the pre-processing phase of the query, would be performed.
			E.g.: 'portuguese'.
	**since** - This parameter is used for the association step. It must be filled in with an initial data that will be composed of query from social media. E.g.: "2000-01-01"
	**until** - This other parameter is complementary to the previous one, establishing a final data for query. E.g.: "2020-08-01".
	**maxTweets** - Indicates the maximum number of tweets that can be collected for each news item. E.g.: "10000".

## Imput file

.\Dataset\LabeledNews.csv - This file contains the result of the collection of news from trusted sources and can be updated through successive executions of this code.

## Output file

.\Dataset\newsFake.csv - This file contains the news labeled fake along with the associations identified between the text of that news and their respective disclosures on Twitter.

.\Dataset\newsNotFake.csv - This file, in turn, contains the news labeled true, along with the associations identified between the text of that news and their respective disclosures on Twitter.

Both output files must be copied to the dataset folder of the next stage of the process, as the output of the second stage is the input of the third.