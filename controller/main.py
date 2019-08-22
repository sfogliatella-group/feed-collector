import twitterGetter
import googleNewsGetter
import time
from datetime import datetime as dt

#Get the query user input
inputQ = input("\nInsert query to search\n")

allTweets = twitterGetter.getTweet(inputQ)
allNews   = googleNewsGetter.getNews(inputQ)

tweetList, secondListT = zip(*allTweets)
newsList, secondListG = zip(*allNews)

dt_listT = []
dt_listG = []

#Conversion of datetime
for i in range(20):
    dt_listT.append(dt.strptime(secondListT[i],'%a %b %d %H:%M:%S +0000 %Y'))
    dt_listG.append(dt.strptime(secondListG[i],'%Y-%m-%dT%H:%M:%SZ'))

allTweets = list(zip(tweetList, dt_listT))
allNews = list(zip(newsList, dt_listG))

allFeedUnsorted = []
allFeedUnsorted = allTweets + allNews
allFeedSorted = sorted(
    allFeedUnsorted,
    key=lambda x: dt.strftime(x[1], '%m/%d/%y %H:%M'), reverse=True
)

for j in range(20):
    print(allTweets[j][0])

#for tweets in range(20):
#    print(tweets, ".", firstListT[tweets])
#
#for news in range(20):
#    print(news, ".", firstListG[news])
#    print(secondListG[news])
