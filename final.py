import pandas as pd
import numpy as np
import re
import tweepy
from textblob import TextBlob

consumer_key='Pj1ktSla52qTXgt61Q7TjbK6b'
consumer_secret='JPu60Ct2473xococU8LiKPtKevpbShqQKYgpq7ISXbVZSKJObU'

access_token='1016812415994875906-WoYwnT7j0Na3NRpuRByHxSGCljFGHj'
access_token_secret='iP5XBVfOhw66K7tX84GoQqGkPa9779hQDMiHgQIuytpS5'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

inp=input("Enter The Text you want to find : ")
public_tweets=api.search(inp,count=100)

sentence_api=np.array([])
polarity_arr=np.array([])
subjectivity_arr=np.array([])


for tweet in public_tweets:

    p=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet.text).split())
    sentence_api = np.append(sentence_api,p)
    analysis = TextBlob(tweet.text)
    nrr=analysis.sentiment.polarity
    if nrr>0:
        nrr='positive'
    elif nrr==0:
        nrr='neutral'
    else:
        nrr='negative'
    polarity_arr=np.append(polarity_arr,nrr)
    subjectivity_arr=np.append(subjectivity_arr,analysis.sentiment.subjectivity)
    dict={'sentence':sentence_api,'polarity':polarity_arr,'subjectivity':subjectivity_arr}

    df_main=pd.DataFrame(dict)

df_main=pd.DataFrame(df_main.dropna())
#print(df_main)
df=pd.DataFrame(df_main.polarity)

df.to_csv('2.csv')





