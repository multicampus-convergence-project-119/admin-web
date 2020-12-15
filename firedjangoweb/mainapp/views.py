from django.shortcuts import render
from urllib import parse
import boto3

def index(request):
    return render(request, 'mainapp/index.html')

def video(request):
    # AWS_REGION = 'us-east-1'
    AWS_STORAGE_BUCKET_NAME = 'fire-video-s3'
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    DATETIME = parse.quote('2020-12-09') # url 형식으로 바꾸어 주기
    FILENAME = '00-00-00.gif'
    VIDEO_URL = 'https://%s/%s/%s' % (AWS_S3_CUSTOM_DOMAIN, DATETIME, FILENAME)
    content = {'static_url': VIDEO_URL }
    return render(request, 'mainapp/video-view.html', content)