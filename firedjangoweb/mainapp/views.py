from django.shortcuts import render
from urllib import parse
import boto3

# AWS S3 버킷 설정
s3_bucket_name = 'fire-video-s3'
s3 = boto3.client('s3')

# AWS S3 end

# main
def index(request):
    return render(request, 'mainapp/index.html')

# 화재감지영상보기
def video(request): 
    # AWS_REGION = 'us-east-1'
    
    filed = get_filenames(s3) # file 이름들을 받아옴

    print(filed)

    AWS_STORAGE_BUCKET_NAME = 'fire-video-s3'
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    DATETIME = parse.quote('2020-12-09') # url 형식으로 바꾸어 주기
    FILENAME = '00-00-00.gif'
    VIDEO_URL = 'https://%s/%s/%s' % (AWS_S3_CUSTOM_DOMAIN, DATETIME, FILENAME)
    content = {'static_url': VIDEO_URL,
    'datetimelist':filed}
    return render(request, 'mainapp/video-view.html', content)


# 지도시각화
def mapview(request): # 빅데이터 지도시각화
    return render(request, 'mainapp/mapview.html', None)
def maptest(request):
    return render(request, 'mainapp/map_object.html', None)
# def mapview(request): 
#     return render(request, 'mainapp/mapview.html')

# 실시간 그래프
def realtime(request): 
    return render(request, 'mainapp/realtime.html')

# video : 영상 날짜/시간 가져오기
def get_filenames(s3):
    filedic = {} # 날짜 : [시간] 을 저장
    result = s3.list_objects_v2(Bucket=s3_bucket_name, Prefix='')
    for item in result['Contents']:
        files = item['Key']
        if len(files) > 12:
            key = files[:10]
            val = files[11:19]
            if key in filedic.keys():
                filedic[key].append(val)
            else:
                filedic[key] = [val]
    return filedic