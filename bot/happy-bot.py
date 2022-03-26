# happy bot
from time import sleep
from httplib2 import Response
import tweepy
import random

bearer_token = ''
api_key = ''
api_key_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(api_key, api_key_secret, access_token=access_token, access_token_secret=access_token_secret, callback=Response)
api = tweepy.API(auth)

def random_phrase():
    p1 = ["felicidade"]

    final_phrase = random.choice(p1)
    return final_phrase

while True:
    api.update_status(status=random_phrase().lower())
    print('-------------------------------------')
    print('um tweet feliz foi enviado com sucesso!')
    print('-------------------------------------')
    sleep(500) # a cada x min