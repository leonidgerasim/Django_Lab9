from django.contrib import admin
from django.urls import path, include
from .views import index, ChartData, create_waybill

app_name = 'lab9'

urlpatterns = [
    path('', index, name='index'),
    path('func/', ChartData.as_view(), name='func'),
    path('create_waybill/', create_waybill, name='waybill')
]