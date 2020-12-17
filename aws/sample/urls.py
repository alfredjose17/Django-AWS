from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .apiViews import PostViewSet
from .views import userView

urlpatterns = [
    path('home/', userView),
    path('home/<str:name>/', userView),
    path('post/', PostViewSet.as_view(), name = 'post')
]