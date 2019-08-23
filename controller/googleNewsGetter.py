import requests

def getNews(query):
    url = ('https://newsapi.org/v2/everything?'
           'q=' + query + '&'
           'from=2019-08-21&'
           'sortBy=popularity&'
           'apiKey=19d001b73d014c9bac431d78db0be537')
    res = requests.get(url)
    gNews = res.json()
    allNews = []
    urls = []

    news = 0
    count = 0

    #Why with while prints even same news
    #and with for prints differents news??? WTF
    #while(news == 0):

    for news in range(10):
        StatusNews = gNews.get('articles')

        if not StatusNews:
            break

        allNews.append(tuple((StatusNews[news].get('title'), StatusNews[news].get('publishedAt'))))
        urls.append(StatusNews[news].get('url'))



    return allNews, urls
