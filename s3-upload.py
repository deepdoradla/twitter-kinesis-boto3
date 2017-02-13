#!/usr/bin/python

import boto3
import json
import boto3.session

session = boto3.session.Session(region_name='eu-west-1')

s3 = session.client('s3',config= boto3.session.Config(signature_version='s3v4'))

result="Hello this is my first s3 object data"

response=s3.put_object(
	Body=result,
	Bucket='deepcloudguru',
	Key='s3consoletest')

print(response)

