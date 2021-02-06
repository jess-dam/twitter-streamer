# the libraries we want to use
import configparser
import tweepy
import twitterlistener

# config.ConfigParser() is used to get the required keys from the twitter.conf file
config_object = configparser.ConfigParser()
config_object.read('./twitter.conf')
keys = config_object["KEYS"]

# Login to Twitter, this tells Twitter that you are using an authorised developer account
auth = tweepy.OAuthHandler(keys["apikey"], keys["apisecret"])
auth.set_access_token(keys["accesstoken"], keys["accesssecret"])

# Create our API connection to talk to Twitter
connection = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


# Request a topic from the user and make sure it is formatted correctly
topic = input("Enter a topic here, and let me find any related tweets on your behalf  •ᴗ• : ")
topic_as_string = str(topic)


# Create our bot that will be listening to the Twitter stream
tweets_listener = twitterlistener.MyStreamListener(connection)

# Create the stream itself, that uses our Twitter login to start collecting tweets that are being posted live
stream = tweepy.Stream(connection.auth, tweets_listener)
stream.filter(track=[topic_as_string], languages=["en"])



