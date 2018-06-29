from picamera import PiCamera
from time import sleep
import time
import boto3
from datetime import datetime

#create an S3 client
s3 = boto3.client('s3')
filename='image.jpg'
bucket_name='pi-cam-5belmont'
camera = PiCamera()
#camera.start_preview()
#time.sleep(10)
camera.resolution=(1024,768)

while True:
    now=datetime.now()
    now=now.strftime("%x_%H").replace('/','_')+'.jpg'
    camera.capture('image.jpg')
    #camera.stop_preview()
    s3.upload_file(filename,bucket_name,now)
    time.sleep(3600)
