from django.urls import path
from . import views
from django.conf import settings

app_name='app'
urlpatterns =[
    path('', views.home, name ='home'),
]