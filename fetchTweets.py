from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


ckey = 'L6rypoEKITm5oBpBomNFuokQM'
csecret = '9ox90xOtrXvYddU595T71YMhk7EHFbqLumJ5zRSw9qxUl9ypDl'
atoken = '4646906597-dxqlK5QKcUCs4r3kXPAB9VqA0uR31q9B06QjDvb'
asecret = '2zMcDflnblXP5iscXZ6CGcPRjDbT6ur1WSUTzQJohJjfw'

class Listener(StreamListener):
    def on_data(self, data):       
        tweet = data.split(',"text":"')[1].split('","source')[0]      
        output = open('output.txt', 'a')
        output.write(tweet)
        output.write('\n')
        output.write('\n')       
        output.close()
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
tStream = Stream(auth, Listener())
tStream.filter(track=["bush"], async=True)
