#!/usr/bin/python

from TwitterAPI import TwitterAPI
import boto3
import json
import twitter_creds

consumer_key = twitter_creds.consumer_key
consumer_secret = twitter_creds.consumer_secret
access_token_key = twitter_creds.access_token_key
access_token_secret = twitter_creds.access_token_secret

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

kinesis = boto3.client('kinesis')

records = api.request('statuses/filter', {'locations':'-90,-90,90,90'})



for item in records:
	kinesis.put_record(StreamName="twitter", Data=json.dumps(item), PartitionKey="filler")
