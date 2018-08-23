from django.urls import path
from . import views
from django.conf import settings

#app_name='app'
urlpatterns =[
    path('', views.home, name ='home'),
    path('delete/<task_id>', views.delete,name='delete'),
    path('edit/<task_id>', views.edit, name ='edit'),
    path('import', views.importcsv, name ='importcsv'),
    path('deleteall', views.deleteall, name ='deleteall'),
]