import  moodAnalyser as mA, readTweets as rt, graphTweets as gt
import time

file = open("output.txt")
if file:
    rT= rt.readTweets(mA)
    gT = gt.graphTweets(rT.getX(),rT.getY())
else:
    import fetchTweets
