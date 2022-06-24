#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import tweepy as tw
import pandas as pd


# In[ ]:





# In[7]:


consumer_key= 'wQm9UJP2FpxQBqOmBBIPjCP0X'
consumer_secret= '2PDEIoZ3qIA2sYZyG2g5XHiLvOQbxRKpMbmJixGmXdrL1W8Ju0'
access_token= '1171806772111269888-yoScVhhG18tUVcYWH8PkuMKtJxGsuj'
access_token_secret= 'kj04cXv5AVsyRisKvGfV740QK6jlLzAMkHkWSWGpJWiTv'


# In[8]:


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


# In[9]:


search_words = "#covid19"
date_since = "2020-01-16"


# In[10]:


tweets = tw.Cursor(api.search_tweets,
              q=search_words,
              lang="en",
              since=date_since,
                  ).items(30000)
tweets


# In[11]:


[tweet.text for tweet in tweets]


# In[12]:


new_search = search_words + " -filter:retweets"
new_search


# In[21]:





# In[14]:


tweets = tw.Cursor(api.search_tweets, 
                           q=new_search,
                           lang="en",
                           since=date_since).items(1000)

users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
users_locs


# In[15]:


tweet_text = pd.DataFrame(data=users_locs, 
                    columns=['user', "location"])
tweet_text


# In[1]:


tweet_text = pd.DataFrame(data=users_locs, 
                    columns=['user',"location"])
tweet_text.to_csv('tweet_text.csv')


# In[ ]:




