from django.shortcuts import render
from urllib import parse
import boto3
from .awsconfig import *


s3_bucket_name = 'fire-video-s3'
s3 = boto3.client('s3',
    region_name=AWS_DEFAULT_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# AWS S3 end

# main
def index(request):
    return render(request, 'mainapp/index.html')

# 화재감지영상보기
def video(request): 
    filed = get_filenames(s3) # file 이름들을 받아옴
    # print(filed)
    if request.method == "POST":
        idd = request.POST.get("select1", None)
        AWS_STORAGE_BUCKET_NAME = 'fire-video-s3'
        AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
        DATE = parse.quote(str(idd[:8])) # url 형식으로 바꾸어 주기
        TIME = parse.quote(str(idd[9:]))
        print(idd[:9], idd[10:])
        FILENAME = 'video.mp4'
        VIDEO_URL = 'https://%s/%s+%s/%s' % (AWS_S3_CUSTOM_DOMAIN, DATE, TIME, FILENAME)
        content = {'static_url': VIDEO_URL,
        'datetimelist':filed , 'datetime':idd, 'DATE':DATE, 'TIME':str(idd[9:])}  
        return render(request, 'mainapp/video-view.html', content)
    return render(request, 'mainapp/video-view.html', {'datetimelist':filed, 'static_url':1})


# 지도시각화
def mapview(request): # 빅데이터 지도시각화
    return render(request, 'mainapp/mapview.html', None)
def maptest(request):
    return render(request, 'mainapp/map_object.html', None)

# 실시간 그래프
def realtime(request): 
    return render(request, 'mainapp/realtime.html')

# video : 영상 날짜/시간 가져오기
def get_filenames(s3):
    filedic = [] # 날짜 : [시간] 을 저장
    result = s3.list_objects_v2(Bucket=s3_bucket_name, Prefix='')
    for item in result['Contents']:
        files = item['Key']
        filedic.append(files[:-10])
        # if len(files) > 9:
        #     key = files[:10]
        #     val = files[11:19]
        #     if key in filedic.keys():
        #         filedic[key].append(val)
        #     else:
        #         filedic[key] = [val]
    return filedic