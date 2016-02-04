from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = stopwords.words("english")
sentiment_neg = open("negative-words.txt","r").read()
sentiment_pos = open("positive-words.txt","r").read()
sentiment_neg = word_tokenize(sentiment_neg)
sentiment_pos = word_tokenize(sentiment_pos)

        
def getTweetMood(tweet):   
    filtered_words = []
    words = word_tokenize(tweet)
    for word in words:
        if word not in stop_words:
            filtered_words.append(word)       
    neutral = 0
    pos_words = 0
    neg_words = 0
    for word in filtered_words:
        if word in sentiment_pos:
            pos_words += 1           
        elif word in sentiment_neg:
            neg_words += 1           
        else:
            neutral = 0           
     
    if pos_words == neg_words == neutral == 0:
        sentiment_value = neutral
    elif pos_words > neg_words:
        value = (pos_words * 100) /len(filtered_words)        
        sentiment_value = value / 10   
    else:        
        value = (neg_words *-100) /len(filtered_words)       
        sentiment_value = value / 10            
    
    return sentiment_value
