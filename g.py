import sys
import csv
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

access_token = "2597236182-0on5ps2a7vF0793UQWbPpXkgGdGzsjKQ2fnhsBw"
access_token_secret = "Kh3I2H5mZNxTkFq10rvA7br5LLSk4QYWqflBpNk83MN0Q"
consumer_key = "AgolVeIZr0Olf3ylWpbRKRCmw"
consumer_secret = "ehoReh0AQwk44HgF4Im33ZN3Tn5BJNDhjY345iTo6nicO3Llg2"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
out=open('harshita6.csv','a')
write=csv.writer(out)


class MyStreamListener(StreamListener):
	def on_data(self, data):
		d = json.loads(data)
		#print d['text']
		print data
		tweet = json.loads(data)
		geo_data = {
		"type": "FeatureCollection",
		"features": []	
		}
		if tweet['coordinates']:
			geo_json_feature = {
			"type": "Feature",
			"geometry": tweet['coordinates'],
			"properties": {
			"text": tweet['text'],
			"created_at": tweet['created_at']
		}
		}

		geo_data['features'].append(geo_json_feature)
 
		
		#u'\u2026'.encode('utf8')
		#write.writerow([d['text']])
        	
       
#myStreamListener = MyStreamListener()
myStream = Stream(auth,MyStreamListener())

if __name__ == "__main__":
	myStream.filter(track=['india'])





