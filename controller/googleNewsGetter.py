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

    for news in range(20):
        StatusNews = gNews.get('articles')
        allNews.append(tuple((StatusNews[news].get('title'), StatusNews[news].get('publishedAt'))))

    return allNews
