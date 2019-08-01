import boto3
import os
import botocore

s3 = boto3.resource('s3', aws_access_key_id = 'AKIA4EPYCMP3QAWE42NJ', aws_secret_access_key = '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')
s3client = boto3.client('s3')

bucket = s3.Bucket('bottle-ml')

files_in_s3 = bucket.objects.all() 

logfile = []

def run_fetch():
	for j in files_in_s3:
		# logfile = open('myfile.txt', 'r')
		if j not in logfile:
			logfile.append(j.key)

	for s in range(len(logfile)):
		# print(logfile[s])
		
		s3.Bucket('bottle-ml').download_file(logfile[s], logfile[s].replace("/", "-"))
		

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