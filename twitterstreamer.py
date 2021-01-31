from configparser import ConfigParser
import tweepy

# This is
config_object = ConfigParser()
config_object.read('./twitter.conf')
keys = config_object["KEYS"]

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")


# Login to twitter, this tells Twitter that you are using an authorised developer account
auth = tweepy.OAuthHandler(keys["apikey"], keys["apisecret"])
auth.set_access_token(keys["accesstoken"], keys["accesssecret"])

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)

# Request a topic from the user
topic_to_find = input(f"Enter a topic here, and let me find any related tweets on your behalf  •ᴗ• : \n")

stream.filter(track=[str(topic_to_find)], languages=["en"])



