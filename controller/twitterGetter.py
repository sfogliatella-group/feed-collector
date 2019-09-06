import requests
from . import config_twitter
from requests_oauthlib import OAuth1

consumer_key='LMjlku3YFTz6iZ8zPggN7A8At'
consumer_secret='z1iDWc34iVMOQIbRMAo4a41NK5TDdvFwXVvuDbMW59nMI855dT'
access_token_key='834036559263461376-7KpnKaq5Bk8c0DSu8fpQtmYy48ACp56'
access_token_secret='YviRSCRxFog119yBdQDDyq10eXLQYXQDKgRto0nBF55Nt'
auth = OAuth1(config_twitter.api_key, config_twitter.api_secret, config_twitter.access_token, config_twitter.token_secret)

def getTweet(query):
    url = 'https://api.Twitter.com/1.1/search/tweets.json' ### url to Twitter JSON
    pms = {'q' : query, 'count' : 100, 'lang' : 'it', 'result_type': 'recent'} ### parameters according to Twitter API
    res = requests.get(url, params = pms, auth=auth)
    tweets = res.json()
    allTweets = []

    stop = 0
    count = 0

    while(stop == 0):
        StatusTweet = tweets.get('statuses')

        if not StatusTweet:
            break
            
        allTweets.append(tuple((StatusTweet[count].get('text'), StatusTweet[count].get('created_at'))))

        count = count + 1

        if(count == 10):
            break


    return allTweets
#TODO Function to get time of tweet
