import twitter

api = twitter.Api(consumer_key='LMjlku3YFTz6iZ8zPggN7A8At',
                  consumer_secret='z1iDWc34iVMOQIbRMAo4a41NK5TDdvFwXVvuDbMW59nMI855dT',
                  access_token_key='834036559263461376-7KpnKaq5Bk8c0DSu8fpQtmYy48ACp56',
                  access_token_secret='YviRSCRxFog119yBdQDDyq10eXLQYXQDKgRto0nBF55Nt')
print(api.VerifyCredentials())
