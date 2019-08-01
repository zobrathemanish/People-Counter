from bottle.centroidtracker import CentroidTracker
from bottle.trackableobject import TrackableObject
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
import json
import boto3
import os
import botocore
import people_counter
import psycopg2 as p


s3 = boto3.resource('s3', aws_access_key_id = 'AKIA4EPYCMP3QAWE42NJ', aws_secret_access_key = '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')
s3client = boto3.client('s3')

bucket = s3.Bucket('bottle-ml')

files_in_s3 = bucket.objects.all() 

logfile = []

log_list = []

all_logs = {}

count = 0

conn = p.connect("dbname = 'peopleCount' user = 'sujal' password = 'hyperl00p' host = 'localhost'")
cur = conn.cursor()

def run_fetch():

	key = 'himab2.mp4'
	cur.execute("INSERT INTO labimcount (videoname, totalpeople) VALUES (%s,%s)", (key, 23))
	conn.commit()
	# rows = cur.fetchall()
	# print(rows)
	# print("Successful Insert")

	# print(all_logs)

run_fetch()
	# key = j.key
	# s3.Bucket('bottle-ml').download_file(key, str())

# key = "24-July-2019/ch02_20190724100000.mp4"

# s3.Bucket('bottle-ml').download_file(key, 'my_local_image.mp4')
# bucket_name = 'bottle-ml'

# camera_id = "02"
# date = "28-July-2019"


# prefix = date + "/" + "ch"+camera_id
# print(prefix)
# for files in s3.Bucket(bucket_name).objects.filter(Prefix=prefix):
#    #subsrc = files.Object()
#    key = files.key
#    print(key)
#    url = "https://s3-%s.amazonaws.com/%s/%s" % (location, bucket_name, key)
#    print(url)
#    boto3.client('s3').download_file(bucket_name, key, key)
#    break


# for bucket in s3.buckets.all():
# 	print(bucket.name)

# files = ['24-July-2019/ch02_20190724100000.mp4']

# for file in files:
# 	s3.Bucket(b"bucket").download_file(file, os.path.basename(file))

# files_in_s3 = bucket.objects.all() 

# for j in files_in_s3:
# 	print(j.key)
# 	s3.Bucket(bucket).download_file('24-July-2019/ch02_20190724100000.mp4', os.path.basename(j.key))