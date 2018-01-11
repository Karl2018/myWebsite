
from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    
    url(r'^$', views.writing),

    url(r'^CatsSongbook.pdf', views.PDF_Request, name= 'CatsSongbook.pdf'),

    

]


