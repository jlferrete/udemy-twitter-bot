import tweepy
import os
from config import create_api
from dotenv import load_dotenv
load_dotenv()


def main():
    api = create_api()
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    #api.update_status(status="Probando un nuevo proyecto de automatización. Este mensaje ha sido generado automaticamente.")


if __name__ == "__main__":
    main()
