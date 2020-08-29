import tweepy
import os
from datetime import datetime

consumer_key = os.environ.get('TWITTER_API_KEY')
consumer_secret = os.environ.get('TWITTER_API_SECRET_KEY')
access_token = os.environ.get('TWITTER_API_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_API_ACCESS_SECRET')
logf = open("errors.log", "w")

try:
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	date = datetime.now()
	date_formated = date.strftime('%d/%m/%Y %H:%M')  
	# Write Tweet
	tweet = 'Angelus. \nAve, gratia plena, Dominus tecum. (Lc 1, 28)\n' + date_formated
	api.update_status(status=tweet)
except tweepy.TweepError as e:
	logf.write(e.response.text)
except tweepy.RateLimitError:
	logf.write("RATELIMITERROR")

