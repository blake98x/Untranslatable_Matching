import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import os
import tweepy as tw
import pandas as pd
import twitter_info

auth = tw.OAuthHandler(twitter_info.consumer_key, twitter_info.consumer_secret)
auth.set_access_token(twitter_info.access_token, twitter_info.access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

stop_words = set(stopwords.words('english')) #define stopwords

def twitter_extract(word,n):
	tweets = tw.Cursor(api.search,q=word + " -filter:retweets",lang="en").items(n)
	tweet_text = [tweet.text.encode('utf-8') for tweet in tweets]
	tokenized_tweets = [word_tokenize(str(tweet,'utf-8')) for tweet in tweet_text]
	for tweet in tokenized_tweets:
		tweet = [w for w in tweet if w.isalpha() and not w in stop_words]
	print(tokenized_tweets)

def main():
	twitter_extract("nostalgia",1)

if __name__ == "__main__":
	main()