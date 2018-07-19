import pandas as pd
import numpy as np
import re
import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt



consumer_key='Pj1ktSla52qTXgt61Q7TjbK6b'
consumer_secret='JPu60Ct2473xococU8LiKPtKevpbShqQKYgpq7ISXbVZSKJObU'

access_token='1016812415994875906-WoYwnT7j0Na3NRpuRByHxSGCljFGHj'
access_token_secret='iP5XBVfOhw66K7tX84GoQqGkPa9779hQDMiHgQIuytpS5'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

inp=input("Enter The Text you want to find : ")
public_tweets=api.search(inp,count=5000)

sentence_api=np.array([])
polarity_arr=np.array([])
subjectivity_arr=np.array([])
positive=0
negative=0
neutral=0

for tweet in public_tweets:

    p=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet.text).split())
    sentence_api = np.append(sentence_api,p)
    analysis = TextBlob(tweet.text)
    nrr=analysis.sentiment.polarity
    if nrr>0:
        nrr='positive'
        positive+=1
    elif nrr==0:
        nrr='neutral'
        neutral+=1
    else:
        nrr='negative'
        negative+=1
    polarity_arr=np.append(polarity_arr,nrr)
    subjectivity_arr=np.append(subjectivity_arr,analysis.sentiment.subjectivity)
    dict={'sentence':sentence_api,'polarity':polarity_arr,'subjectivity':subjectivity_arr}

    df_main=pd.DataFrame(dict)

df_main=pd.DataFrame(df_main.dropna()) 
list=np.array([neutral,positive,negative])
new_df=pd.DataFrame(list,index=['Neutral','Positive','Negative'],columns=['Sentiment'])

plt.pie(new_df,labels=['Neutral','Positive','Negative'],explode=[0.1,0.1,0.1])
plt.show()
df_main.to_csv('details.csv')





