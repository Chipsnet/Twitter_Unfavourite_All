"""
Use this to remove all of your followers on Twitter. It seems it is easy to gather 
followers but not so easy to get rid of them, I wonder if Jesus ever felt this way. 

Disclaimer: Use at your own risk. I am not responsible for anything that goes wrong.
Don't be an idiot; the cardinal rule. 

To run you must create an application at https://apps.twitter.com and get the consumer 
and consumer secret keys. You must also create both access and access secret tokens on 
the same page. Enter these keys below. 

"""
import tweepy

consumer_key = "#"
consumer_secret = "#"
access_token = "#"
access_token_secret = "#"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

batch_number = 100

favs = api.favorites(count=batch_number)
num_destroyed = 0
while len(favs) > 0:
	for f in favs:
		api.destroy_favorite(f.id)
		num_destroyed += 1
		if num_destroyed % 100 == 0:
			print("{} favourites have been destroyed".format(num_destroyed))
	favs = api.favorites(count=batch_number)

print("{} favourites destroyed in total".format(num_destroyed))