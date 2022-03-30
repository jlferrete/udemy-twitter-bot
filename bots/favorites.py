import tweepy
import os
import logging
from config import create_api
from dotenv import load_dotenv
load_dotenv()


def main():
    api = create_api()
    tweet_list = api.favorites(screen_name='Jlferrete', count=5)
    # print(tweet_list)

    # print the id for each of the tweets
    for tweet in tweet_list:
        print(tweet.id)


if __name__ == "__main__":
    main()
