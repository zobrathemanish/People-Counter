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

totalCount = 0

def run_fetch():	
	g = input("Please insert the date: ") 
	print(g)
	for j in files_in_s3:
		# logfile = open('myfile.txt', 'r')
		if j not in logfile:
			logfile.append(j.key)

	for s in range(len(logfile)):
		# print(logfile[s])
		suffix = g
		endfix = "mp4"
		flag1 = logfile[s].startswith(suffix)
		flag2 = logfile[s].endswith(endfix)

		if(flag1 == True):
			if(flag2 == True):
		
				s3.Bucket('bottle-ml').download_file(logfile[s], 'now_video.mp4')
				total_people = people_counter.main('now_video.mp4')
				key = str(logfile[s])
				all_logs[str(logfile[s])] = total_people

				print("Total People Count is done")
			
				cur.execute("INSERT INTO labimcount (videoname, totalpeople) VALUES (%s,%s)", (key, total_people))
				conn.commit()

				cur.execute("SELECT SUM(totalpeople) FROM labimcount WHERE labimcount.videoname LIKE '24-July-2019%';")
				conn.commit()
				print("Successful Insert")

	print(all_logs)

run_fetch()
	

insert into student3_total(s_id,mark) select id, sum(math + social +science) from student3 group by id

CREATE TABLE playground (
    equip_id serial PRIMARY KEY,
    type varchar (50) NOT NULL,
    color varchar (25) NOT NULL,
    location varchar(25) check (location in ('north', 'south', 'west', 'east', 'northeast', 'southeast', 'southwest', 'northwest')),
    install_date date
);