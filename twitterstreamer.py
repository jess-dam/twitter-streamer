import configparser
import tweepy
import twitterlistener

# This part is used to get the required keys from the twitter.conf file
config_object = configparser.ConfigParser()
config_object.read('./twitter.conf')
keys = config_object["KEYS"]


# Login to Twitter, this tells Twitter that you are using an authorised developer account
auth = tweepy.OAuthHandler(keys["apikey"], keys["apisecret"])
auth.set_access_token(keys["accesstoken"], keys["accesssecret"])

# Create API object to talk to Twitter
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


tweets_listener = twitterlistener.MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)

# Request a topic from the user
topic_to_find = input("Enter a topic here, and let me find any related tweets on your behalf  •ᴗ• : ")

stream.filter(track=[str(topic_to_find)], languages=["en"])



