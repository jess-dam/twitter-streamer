import tweepy

# tweepy.StreamListener is Tweepy's own blueprint which creates an object that will listen out for live tweets
# We can customise tweepy.StreamListener by creating our own class (MyStreamListener) on top of it, which will update the blueprint for the functions we specify
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api

    def on_status(self, tweet):
        print(f"{tweet.user.name}: {tweet.text}")

    def on_error(self, error):
        print("An error has occurred: ", error)