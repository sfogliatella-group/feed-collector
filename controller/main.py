import twitterGetter
import googleNewsGetter
import time
from datetime import datetime as dt

#Get the query user input
inputQ = input("\nInsert query to search\n")

allTweets = twitterGetter.getTweet(inputQ)
allNews, urlNews = googleNewsGetter.getNews(inputQ)

def twitter_res(listTweets):
    tweetList, secondListT = zip(*listTweets)
    dt_listT = []
    for i in range(10):
        dt_listT.append(dt.strptime(secondListT[i],'%a %b %d %H:%M:%S +0000 %Y'))

    listTweets = list(zip(tweetList, dt_listT))

    for j in range(10):
        print(listTweets[j][0])

def google_res(listNews):
    newsList, secondListG = zip(*listNews)
    dt_listG = []

    #Conversion of datetime
    for i in range(10):
        dt_listG.append(dt.strptime(secondListG[i],'%Y-%m-%dT%H:%M:%SZ'))

    listNews = list(zip(newsList, dt_listG))

    for k in range(10):
        print(listNews[k][0])
        print("URL: ", urlNews[k])


if allTweets and allNews:
    twitter_res(allTweets)
    google_res(allNews)

elif allTweets and (not allNews):
    twitter_res(allTweets)

elif (not allTweets) and allNews:
    google_res(allNews)

elif (not allTweets) and (not allNews):
    pass
    print("No news")
