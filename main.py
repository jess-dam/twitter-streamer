# The libraries we'll be using
import tweepy
import twitterlistener

# 1. Login to Twitter, this tells Twitter that you are using an authorised developer account
# You can find these keys in your Twitter developer account
auth = tweepy.OAuthHandler("yourapikey", "yourapisecret")
auth.set_access_token("youraccesstoken", "youraccesssecret")

# 2. Create our API connection to talk to Twitter
connection = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# 3. Create our bot that will be listening to the Twitter stream
tweets_listener = twitterlistener.MyStreamListener(connection)

# 4. Create the stream itself, that uses our Twitter login to start collecting tweets that are being posted live
stream = tweepy.Stream(auth, tweets_listener)
stream.filter(track=["a topic to search for"])



