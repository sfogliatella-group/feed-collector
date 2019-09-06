from controller.feedGetter import twitter_res
from controller.feedGetter import google_res
from controller.googleNewsGetter import getNews
from controller.twitterGetter import getTweet

#Get the query user input
inputQ = input("\nInsert query to search\n")

allTweets = getTweet(inputQ)
allNews, urlNews = getNews(inputQ)

print("\n")
if allTweets and allNews:
    twitter_res(allTweets)
    print("\n")
    google_res(allNews)

elif allTweets and (not allNews):
    twitter_res(allTweets)

elif (not allTweets) and allNews:
    google_res(allNews)

elif (not allTweets) and (not allNews):
    pass
    print("No news")