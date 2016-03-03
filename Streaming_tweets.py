'''
    Author: Harshita Sharma
    Date: 3/3/2016
'''

#importing packages
import sys
import csv
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Twitter credentials generated from twitter account
access_token = "<...>"
access_token_secret = "<...>"
consumer_key = "<...>"
consumer_secret = "<...>"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

out=open('harshita6.csv','a')
write=csv.writer(out)


class MyStreamListener(StreamListener):

	def on_data(self, data):					''' prints all the Live tweets stream '''
		d = json.loads(data)
		print(d['text'])
		print(d['place'])
		x = (d['text'])
myStream = Stream(auth,MyStreamListener())

if __name__ == "__main__":
	
	myStream.filter(track=['python'])     				''' filter out tweets containing word "python" '''
	
    	def getText():
	csvFile = open('swathi.csv', 'a')
	csvWriter = csv.writer(csvFile)
		

        # Cleans Text
        clean_Extracted_Tweets()

        # # Removes Stopwords
        removeStopWords()
        
	# # Tokenize Tweets
	TweetTokenizer()
       
        # Returns Tokenized Tweets stored in edit_0.csv 
        return None
        

	def clean_Extracted_Tweets(x):
		i=0
		with open('harshita6.csv') as inp, open('edit_0.csv','a') as out:
			reader = csv.reader(inp,delimiter=' ')
			writer = csv.writer(out,delimiter=' ',escapechar=' ', quoting=csv.QUOTE_NONE)
			for k in reader:
		
				l=''.join(k)
		
				match = re.search(r'^RT\W', l)			'''Retweets removal '''
				t=re.sub(r'(https:\/\/t.co\/\S+)+',"",l)	''' regex for removing noise "http..." '''
				n=re.sub(r'http',' ',t)			
				y=re.sub(r'(#\w*)',' ',n) 			''' #hashtag removal '''
				w=re.sub(r'[\,\.]'," ",y)			''' punctuation marks removal'''
				wx=re.sub(r'^\s*$',"",w)
				wxx=re.sub(r'^\s*$',"",wx)
				b=re.search(r'[^\x00-\x7F]+',l)			 '''unicode removal '''
				o=(wxx).split()

			if not match and not b:
				writer.writerow(o)
	return None


	def TweetTokenizer():
		stop_words = (stopwords.words('english'))			 '''StopWord removal '''

		filtered=[]
		with open('edit_0.csv', newline='') as f:
    		reader = csv.reader(f)
   	 	#word_tokens = word_tokenize(reader)
    		for w in reader:
    			if w not in stop_words:
	    			filtered.append(w)

		csvFile = open('edit_0.csv', 'a')
		csvWriter = csv.writer(csvFile)
		for g in filtered:
			csvWriter.writerow(g)
	return None

	def removeStopWords():
		myStream.filter(track=['cricket'])
		stop_words = (stopwords.words('english'))
		filtered=[]
		with open('edit_0.csv', newline='') as f:
			reader = csv.reader(f)
	return None
   	 	


















