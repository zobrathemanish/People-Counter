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
	bet_suffix = g + "%"

	for j in files_in_s3:
		# logfile = open('myfile.txt', 'r')
		if j not in logfile:
			logfile.append(j.key)

	for s in range(len(logfile)):
		# print(logfile[s])
		suffix = g
		bet_suffix = suffix + "%"
		endfix = "mp4"
		flag1 = logfile[s].startswith(suffix)
		flag2 = logfile[s].endswith(endfix)

		if(flag1 == True):
			if(flag2 == True):

				date = logfile[s].rsplit('_', 1)[-1]

				yy = date[0:4]
				mm = date[4:6]
				dd = date[6:8]
				hrs = date[8:10]
				mins = date[10:12]
				sec = date[12:14]

				final_date = yy + '-' + mm + '-' + dd
				final_time = hrs + ":" + mins + ":" + sec

				s3.Bucket('bottle-ml').download_file(logfile[s], 'now_video.mp4')
				total_people = people_counter.main('now_video.mp4')
				key = str(logfile[s])
				all_logs[str(logfile[s])] = total_people

				print("Total People Count is done")
			
				cur.execute("INSERT INTO labimcount (videoname, totalpeople, date, starttime) VALUES (%s,%s,%s,%s)", (key, total_people, final_date, final_time))
				conn.commit()

				print("Successful Insert")

	cur.execute("INSERT INTO peoplecountperday (totalpeople) SELECT SUM(totalpeople) FROM labimcount WHERE labimcount.videoname LIKE %s;", (bet_suffix,))
	conn.commit()

	print("Total sum of the video is done")

	cur.execute("UPDATE peoplecountperday SET date = %s WHERE date IS NULL;", (suffix,))
	conn.commit()
	print("Total People Count of a day is done")	


run_fetch()
	

# UPDATE raju1 SET video_name = '24-July-2019' WHERE video_name IS NULL;

# 20190724100000.mp4

