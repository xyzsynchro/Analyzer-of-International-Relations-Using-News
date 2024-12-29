<h1>Analyzer of International Relations Using News</h1>

Note: This work was initially made as a graduation project, and it is significantly edited to be used in readme.md.

<h2>Abstract</h2>

The purpose of work study is to analyze international relations between leading
countries in the world, based on news and formal press statements published by
several sources from countries around the world, using natural language processing 
(NLP) techniques including sentiment analysis, mainly using VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool. 
News give us a broad idea of countries’ view towards each other, whether it be the formal view of government or the people’s
view living in that country. By implementing a project which can evaluate the
sentimental content of those news, automating the process of international relation
analysis can be aimed, and the burden of human work created by analyzing news one
by one may be reduced.

<h2>Introduction</h2>
This project’s main goal is analyzing countries’ relationships with another countries
by sentiment analysis and examine if they are good or bad. News from a country’s
news agencies or newspapers are good signs to lead to that decision. To perform the
analysis, some pre-collected data and newly collected data are used. By this action,
the news data has been enlarged and also updated.  
The newly collected news are the news that have been added to the websites
of newspapers’ in general between 1 June and 1 December 2021. Only news with
political content have been picked and added to the data list. The only problem
about collecting the data was, most of the news were about COVID-19 and most of the news were focused on
COVID positive case numbers and effectiveness of COVID-19 vaccines.  
After collecting data, right tools to perform analysis has been researched. Detailed
information about used tools, programming languages and news resources are
explained during the report.

<h2>Preliminary Examination</h2>
Published works about sentiment analysis have been searched. The findings are;
that the technique is commonly used for Twitter view analysis, product review
analysis and movie review analysis. Our topic specifically revolves around
the news, and in recent years there have been some published works involving the
sentiment analysis of the news. Sentimental analysis of the
news differ from the reviews, in a way that a review’s content is generally more
subjective and the target of a review is clearly defined, unlike news. This makes
the sentiment analysis of news slightly more complex, compared to the analysis of a
product/movie review. When we searched for works involving the sentiment analysis
of news specifically designed around international relations, we could not find such
kind of work aiming to find "score"s between the countries.

<h2>Methodology</h2>
The steps we take in this project can be summarized as: Deciding in what format and
method to collect the news, collecting and storing the news from different kind of
news sources on internet, formatting the sentences in the headers and the bodies of
those news, analyzing those sentences by how much they are leaned towards positive
or negative, calculating a summary of scores based on the news between each country
pair, and build an interface to visualize the final international relation scores on a
user-friendly and interactive map.  

Sentiment analysis is a method of natural language processing, aiming to calculate
the sentiment of a given text. Different uses of it includes, but not limited to, the
evaluation of a given sentence or any length of given text as positive, neutral, or
negative; or determining how it scales about its objectivity and subjectivity.  

<h3>Selecting the Countries</h3>
As collecting the news around over 200 countries in the world would be too difficult,
the need to limit the set of countries was obvious. The chosen country set for our
study includes United States, Canada, United Kingdom, France, Germany, Italy, Russia,
Japan, China and Iran. The first 8 countries stated first make up the group called G8
countries. We aimed to pick foremost countries in the world. The reason for that
are, people mostly tend to have knowledge about the international relations between
those countries, and there are much more news published between, compared to other
countries. One other reason is, English news sources between other countries may be
limited.

<h3>Collecting the News</h3>
We have focused on news sources from the countries we picked. Our methods
include browsing the political section of the most famous newspapers of selected
countries previously stated in this paper, and using Google search, Google News
and DuckDuckGo News. Also, 
The initial data set consists of news published mostly around late 2010s. Our aim
was strengthening this data set with more news, especially from 2021.
The way  news are collected is saving the headers and bodies (separately),
publish date, the source country and the target country of each news.
To collect the news, we decided to use each country’s state-run news agencies, if there
is any. If not, the news source closest to the government. If neither of them has an available
news source web page, we have collected news from one of the most recommended
news page for that country.  

The news sources used to collect news for our data set to analyze countries’ relations
are listed below:  
• Canada : Global News Canada (recommended)   
• China : Xinhua News Agency (official state press agency)  
• France : France24 (state owned press agency)   
• Germany : Deutsche Welle (state owned press agency)  
• Iran : Islamic Republic News Agency (government-controlled news agency)  
• Italy : The Local Italy (recommended)  
• Japan : Japan Times (recommended)  
• Russia : TASS - Information Agency Russia (state-owned press agency)  
• United Kingdom : BBC (major news source)  
• United Stated : CNN (major news source)  
When needed, other foremost news sources were also used.

<h3>Analyzing the Data</h3>

For each country pair, a summary of sentiment scores of news between those countries
are calculated. As we picked 10 countries for the basis of this project, an 10x10
matrix is where those scores are stored. Also, a country’s view about an other country
may be different from that other’s country’s view to this particular country. So the
relations of each country is actually 2-way.  
We apply NLP techniques such as tokenizing and subject extraction to pre-process the
loaded data, before the sentiment analysis.  
VADER (Valence Aware Dictionary and sEntiment Reasoner) and TextBlob are
examined for implementing sentiment analysis in this project. TextBlob is a Python
library for common natural language processing (NLP) tasks such as part-of-speech
tagging, sentiment analysis, classification and translation etc. VADER is a simple
rule-based model for general sentiment analysis[8], which also is a Python library. It
is specifically attuned to sentiments expressed in social media.

TextBlob evaluates the polarity of a text’s sentiment and scores them between
-1 and 1, where -1 is the extreme negative and 1 is the extreme positive. It also
calculates the subjectivity between the range 0 and 1, where 0 is very objective and 1
is very subjective.  
VADER takes each word in the text into account. In its lexicon, words are stored
with their valence scores. So, when a sentence is being evaluated, the consisting
words are looked up in the dictionary and a sentiment score is calculated. ’pos’,
’neu’, ’neg’ scores show us the proportion of positive, neutral and negative words in a
text, respectively. The ’compound’ score is calculated as previously told, by summing
the valence scores of each word, and normalising it between -1 and 1, where -1 is
negative and 1 is positive.  
When we examined both options, we found out that VADER is a better option
compared to TextBlob for this project. The reason is; while often TextBlob calculates
a point 0 often for a news, VADER can successfully evaluate if a news is positive or
negative. Further testing of VADER will be showed in figures in later chapters.

<h3>Testing VADER</h3>

This part is about the process of testing how successful VADER evaluates the
news about their positivity and negativity, without applying any kind of other natural
language processing operations, such as lemmatizing, stemming or stop word removal.
We picked a portion of news that we collected for our dataset to test VADER.
This chosen sample includes 38 news, all from Japan-based sources. Then we
evaluated each of those news if they are overall positive or negative towards the
target country and saved under ’actual’ column; 1 for positive and -1 for negative.
Then we combined the ’header’ and ’bodies’ of the news and saved their VADER
’compound’ score under ’compound’ column. Then, if the compound score is positive
we saved it as 1 under the column ’vader’, and -1 if it’s negative (shown in figure below).  


Then we compared the scores given by human decision and VADER evaluation and
saved it under the column ’success’; ’True’ if they agree with each other and ’False’
if they don’t. We calculated the success rate of VADER by finding the percentage of
’True’s under this column. The success rate for this sample set of data is 76.3% (shown
in figure below).  

<h3>Loading the Data</h3>
As previously mentioned, our news data set we improved and worked on includes
header, body, publish date, the two-letter country code based on the news agency of
the published news, and the two-letter country code of country the news is about. We
prepared two files; the first one includes all the news in the dataset, both between
2018-2020 and second half of 2021. The second file includes only the recent news published
in the second half of 2021. This way, relations between countries can be analyzed both in general and
for the near time period. Selected file is loaded to a Pandas dataframe.  

<h3>Checking the Subjects</h3>
As there is a possibility the manually retrieved data may have wrong country codes
for their content, we decided to design a method to correct those.   
The way we modeled it should have worked like this: if the subject of a header of the news is not
connected to the countries originally saved under either ’from’ and ’to’ columns, and
also if the subject is connected to other eight countries we used for this project, then
’to’ column should be altered as the country code of that country.  

Altering the 'from' column is another alternative, but the way the data set was collected,
’from’ column is always based on the country of news agency publishing the news, and it is assumed that the sentiment
belongs to the country which publishes the news.  

Firstly, key words for every country are created, which could be the subjects in
the header of the news. Example subjects keywords for America includes ’U.S.’, ’US’,
’America’, ’Washington’, ’Joe Biden’, ’Donald Trump’. Subjects found in the header for
each news are then searched in keywords of ’from’ and ’to’ country. If they are found
in those, then it is assumed correct and nothing is changed. If not, they are searched
in the keyword lists of other countries. If found, the ’to’ is changed to that country. If
they are not found in any keyword list, the ’to’ country is not changed, as it is normal
that a header doesn’t contain any of those keywords.  

For finding the subjects of headers, spaCy is used. spaCy is another library
in Python for applying Natural Language Processing techniques. spaCy can create the
dependency tree of a given sentence, and the dependency "nsubj" is the subject.  

Figure below  shows an example of subject correcting applied successfully. The news
header ’Russia, Germany hope efforts to save Iran nuclear deal will be continued.’
initially has CH (China) as the country the news is about. But our model changed it
to DE (Germany).

<h3>Calculating VADER Score</h3>
Before calculating the average sentiment score, firstly a new column is created
by appending the body of news to the header. This way, both part of the news are
taken into account when calculating the score. This new column is maned as ’full text’.
The full text of each news is then used to calculate the VADER sentiment compound
scores. As mentioned before, in VADER’s lexicon, words are stored with their valence
scores. Valence scores are summed and normalized to calculate the compound score
of a sentence.

<h3>Tokenizing</h3>

If the tokenizing option is active, news paragraph is tokenized into sentences before
applying VADER sentiment analysis. If selected this way, each sentence is taken into
account separately. VADER is applied to each sentence one by one and then the average
score for each sentence is calculated to find out the score for that news. For the
tokenizing, Natural Language Toolkit (NLTK) is used[10]. NLTK is a library in Python
for appyling Natural Language Processing.

<h3>Calculating Average Scores</h3>

After calculating the VADER scores for each news, what is left to do is grouping by
country pairs and calculating average scores of news between. Output of this is the
10x10 matrix, 2-way between each country pair. This relation matrix is then saved to
an Excel file, ready to be used by the interface module.

<h3>Visualization</h3>
To create user interface, a Python package called "Tkinter" has been used. While
creating the map, a Python package called "Geopandas" and to show the map
"Matplotlib.pyplot" package have been used.  

At first, the user is greeted with a basic user interface. In this interface, three
decisions are to be made. One for selecting target country, one for selecting time
period -All the data or specifically collected during this project’s period- and one for
selecting view point -News from the selected country or news about the selected
country. With this selection, a plot shows up to the screen with a world map and
paints the countries based on calculated relations. If index is positive, it shows good
relations. If index is negative, it shows bad relations. Other countries exempt from
this project are initialized with zero.  

<h2> Experimental Results </h2>
In this example shown in figure below; user has selected United Kingdom as country,
’all the data’ as time range and ’others’ vision’ as the point of view. With this result,
it is possible to make a comment as "Japan, compared to other countries, has better
relations with the United Kingdom.". Also, we can see that all of the countries look
United Kingdom positively -except Canada-. The legend has mostly
positive values and all of the countries has more yellowish color than violet purple
(0 value).  

If we change the point of view to UK, a result like the figure below is shown.
We can see that United Kingdom looks none of the other countries positively, but the negativity reaches higher with Russia, Iran and China.  

When we change the dataset to last 6 months (2021/06-12), we can see that United Kingdom's point of view Russia, Iran and China
persists, and also the sentiment to France is generally more negative. This is caused by the news concerning the fishing dispute news which was caused by Brexit (2021 Jersey Dispute).  

<h2>Conclusion</h2>
The given results show us that VADER is accurate with straightforward relationships.
For example; Russia, China and Iran generally have positive scores to each other,
as like how they have been viewed as political allies. Meanwhile, those countries’
relations with United States and the United Kingdom is lower, compared to other
countries. Also, it is possible to see specific events causing the polarity in the scores,
such as the detention of two Canadian citizens in China causing the drop in the scores.  

Our world and relations between countries are very complex. There might be an
ongoing historical problem but the vast amount of news to ease the tension can cause
the relations to be calculated actually as positive. Another example is, specifically
during the COVID-19 pandemic, the countries had lots of opportunities to manage the
results of the pandemic as they wanted. For example, maybe United States wanted
to close its borders to Iranian citizens, but there was no big reason to do it until the
pandemic.  

Another issue can be that countries viewed friendly bringing travel restrictions to each other
can cause the news look negative. In this case, using common sense helps us to identify
things as good or bad. Without it the results can give us a piece of information but
may not give the real one.  

VADER is a powerful tool to perform sentiment analysis, especially if the text is
subjective, sentimental, and straightforward enough. However, the news are formal
by their nature. Also; positive, negative and neutral sentences all can be included
in the same news. 

In conclusion, this project can be a good guide for us to perceive understand relations of
countries and viewing them on the map, if the news dataset about the wanted timeframe is provided  
