from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('video/', views.video, name='video'), # 화재감지영상보기
    path('realtime/', views.realtime, name='realtime'), # 실시간 그래프그리기
    path('mapview/', views.mapview, name='mapview'), # 지도시각화
]