from django.contrib import admin
from django.urls import path, include
from .views import index

app_name = 'lab9'

urlpatterns = [
    path('', index, name='index'),
    path('func/', ChartData.as_view(), name='func')
]