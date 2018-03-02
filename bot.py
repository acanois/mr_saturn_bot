import tweepy
import credentials as cfg
import random
import time	
from saturn_words import *

auth = tweepy.OAuthHandler(cfg.consumer_key, cfg.consumer_secret)
auth.set_access_token(cfg.access_token, cfg.access_token_secret)

api = tweepy.API(auth)

# Randomizes upper and lower case letters. Because Mr. Saturn talks like that.
def saturnize(word):
	for c in word:
		if (random.random() > 0.5):
			return c.upper()
		return c.lower()

def create_post():
    suffix = random.choice(suffixes)
    properNoun = random.choice(nnp)
    noun = random.choice(nn)
    pluralNoun = random.choice(nns)
    adjective = random.choice(jj)

    saturnNoun = ''.join(map(saturnize, properNoun))
    saturnAdj = ''.join(map(saturnize, adjective))
    saturnNoun = ''.join(map(saturnize, noun))
    saturnPlNoun = ''.join(map(saturnize, pluralNoun))
    saturnSuffix = ''.join(map(saturnize, suffix))

    post = saturnNoun + " " + saturnAdj + " " + saturnSuffix
    return post

while(True):
    post = create_post()
    print(post)
    api.update_status(post)
    time.sleep(60)