import csv

import configparser
import tweepy


APIkey = '4Y5k6QMuzK84Qck4gUAQjB4ny'
APIsecret = 'JSSRqlpEgsP1eL0fADJMXtOIVH2KUAS6E2QoEhX4CFeEAFmtaj'
accessToken = '13459402-63MJNzZAbfTTDv6BbMGoKJsp48jj0mVC5dw7R4cLw'
accessSecret = 'kawMydhDAcsKEEno7fshYD2cZxQsakH4TaM6XqlQOPM0h'
auth = tweepy.OAuthHandler(APIkey,APIsecret)
auth.set_access_token(accessToken,accessSecret)


api = tweepy.API(auth)

public_tweets = api.home_timeline()
i=0
for tweet in public_tweets:
    print(tweet.)
    print(tweet.text)
    i = i+1
    if (i==10):
        break
