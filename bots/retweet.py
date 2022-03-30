import tweepy
import os
import logging
from config import create_api
from dotenv import load_dotenv
load_dotenv()


# tweet_list = api.favorites(screen_name='DavidDobrik', count=5)
# print(tweet_list)

# print the id for each of the tweets
# for tweet in tweet_list:
# print(tweet.id)

# retweet a tweet.id
# tweet_id = 1231720300724793344
# api.retweet(tweet_id)

# retweet each teet

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def main():
    api = create_api()
    for tweet in api.favorites(screen_name='Jlferrete'):
        try:
            api.retweet(tweet.id)
        except tweepy.TweepError as e:
            print(e)


if __name__ == "__main__":
    main()
