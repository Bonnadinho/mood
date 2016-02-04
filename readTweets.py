# this class takes a parameter moodAnalyser
# dependent on the Module MoodAnalyser

class readTweets():
    __moodAnalyser = None
    __xAs = []
    __yAs = []    

    def __init__(self, moodAnalyser):
        self.__moodAnalyser = moodAnalyser       
        
        twitterFeeds = open("output.txt","r").read()
        tweets = twitterFeeds.split("\n")
        counter = 0
        for tweet in tweets:
            counter += 1
            self.__xAs.append(counter)
            sentiment_value_of_tweet =  self.__moodAnalyser.getTweetMood(tweet)
            self.__yAs.append(sentiment_value_of_tweet)   
    
    def getX(self):
        return self.__xAs

    def getY(self):
        return self.__yAs
