from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^process_post/$', views.process_post, name='process_post'),
    url(r'^posts/$', views.posts, name='posts'),
]