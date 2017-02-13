#!/usr/bin/python

import boto3
import time
import json
import boto3.session

session = boto3.session.Session(region_name='eu-west-1')

s3 = session.client('s3',config= boto3.session.Config(signature_version='s3v4'))

kinesis = boto3.client("kinesis")
s3 = boto3.client("s3")

shard_id = "shardId-000000000000" #This is the shard id for the first shard
latest_shard_iterator = kinesis.get_shard_iterator(StreamName="twitter", ShardId=shard_id, ShardIteratorType="LATEST")
shard_iterator = latest_shard_iterator["ShardIterator"]
i=1
while i<15:
     twitter_record = kinesis.get_records(ShardIterator=shard_iterator, Limit=1)
     shard_it = twitter_record["NextShardIterator"]
     for record in twitter_record['Records']:
     	text = json.loads(record['Data'])['text']
     	print(text)
     	s3response = s3.put_object(
			Body=text,
			Bucket='kinesis-dev',
			Key=str(i))
     
     print("Reading stream record " + str(i))
##     print twitter_record
     i=int(i)+1
     time.sleep(1.0)
