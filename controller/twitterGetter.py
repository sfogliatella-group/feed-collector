import requests
from requests_oauthlib import OAuth1

consumer_key='LMjlku3YFTz6iZ8zPggN7A8At'
consumer_secret='z1iDWc34iVMOQIbRMAo4a41NK5TDdvFwXVvuDbMW59nMI855dT'
access_token_key='834036559263461376-7KpnKaq5Bk8c0DSu8fpQtmYy48ACp56'
access_token_secret='YviRSCRxFog119yBdQDDyq10eXLQYXQDKgRto0nBF55Nt'
auth = OAuth1(consumer_key, consumer_secret, access_token_key, access_token_secret)

def getTweet(query):
    url = 'https://api.Twitter.com/1.1/search/tweets.json' ### url to Twitter API
    pms = {'q' : query, 'count' : 100, 'lang' : 'it', 'result_type': 'recent'} ### parameters according to Twitter API
    res = requests.get(url, params = pms, auth=auth)
    tweets = res.json()
    allTweets = []
    
    for tweet in range(20):
        StatusTweet = tweets.get('statuses')
        allTweets.append(tuple((StatusTweet[tweet].get('text'), StatusTweet[tweet].get('created_at'))))
    return allTweets
#TODO Function to get time of tweet
