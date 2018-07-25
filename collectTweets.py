from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import urllib
class listener(StreamListener):
    def on_data(self,data):
        file = open("tweets.json","a")
        file.write(data + "\n")
        file.close()
        print("Record Saved")
        return(True)
    def on_error(self,status):
        print(status)

auth = OAuthHandler("HcMuLYv8KY9ZXqWeE5uUuKCuh","FHQQJHM4VyrtbCH5K5mE68GISDHGtRcObuAADUyWenPjDsA7u8")
auth.set_access_token("3075477583-6gzI0YUSF0pGJ8hOgxS7QIn2RFoSCaQKVYgbCTb","17w4w9E3ch6zkffbAoBHnH9ATzoseQ9uj6mKkSSOqE2AQ")
stream = Stream(auth,listener())

##alltweets = []	
##new_tweets = api.user_timeline(screen_name = screen_name,count=200,tweet_mode = 'extended')
##alltweets.extend(new_tweets)
##stream.filter(track =["UNESCO","Jana Gana Mana","Best National Anthem"])

        
stream.tweet.user.name
