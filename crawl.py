#!/usr/bin/env python
# encoding: utf-8

import tweepy
import csv

consumer_key = "HcMuLYv8KY9ZXqWeE5uUuKCuh"
consumer_secret = "FHQQJHM4VyrtbCH5K5mE68GISDHGtRcObuAADUyWenPjDsA7u8"
access_key = "3075477583-6gzI0YUSF0pGJ8hOgxS7QIn2RFoSCaQKVYgbCTb"
access_secret = "17w4w9E3ch6zkffbAoBHnH9ATzoseQ9uj6mKkSSOqE2AQ"


def get_all_tweets(screen_name):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret) # Authorising with the consumer credentials
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	alltweets = []	
	new_tweets = api.user_timeline(screen_name = screen_name,count=200,tweet_mode = 'extended')
	alltweets.extend(new_tweets)
	oldest = alltweets[-1].id - 1
	
	while len(new_tweets) > 0:
		
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest,tweet_mode = 'extended') # getting all tweets from a new user
		alltweets.extend(new_tweets) # appending to all tweets which will be used for printing time in a new file
		oldest = alltweets[-1].id - 1
		
			
	outtweets = [[tweet.created_at] for tweet in alltweets]
	
	file = csv.writer(open('%s.csv'%screen_name,'w',encoding='utf-8'))
	for tweet in alltweets: #printing text into a new file
		file.writerow([tweet.full_text])

	with open('time_%s.csv'%screen_name,'w',encoding='utf-8') as f: # printing time into a new file
		writer = csv.writer(f)
		writer.writerow(["created_at"])
		writer.writerows(outtweets)

	print("DONE")
	
	pass

if __name__ == '__main__':
	
	file = csv.reader(open("users.csv","r")) # reading list of users
	arr_users = []
	for users in file:
		arr_users.append(users[0]) # storing all the users in  a new array
	for users in arr_users:
		get_all_tweets(users)
