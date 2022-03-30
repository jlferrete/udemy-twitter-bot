import tweepy
import os
import logging
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# tweepy retweet likes function
def retweet_favorites(api, username):
    for tweet in api.favorites(username, count=10):
        try:
            api.retweet(tweet.id)
        except tweepy.TweepError as e:
            print(e)
    return print("done.")


def main():
    api = create_api()
    retweet_favorites(api, 'jlferrete')


if __name__ == "__main__":
    main()
