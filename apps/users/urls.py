from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_validate/$', views.login_validate, name='login_validate'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register_validate/$', views.register_validate, name='register_validate'),
    url(r'^logout/$', views.logout, name='logout'),
    # url(r'^create_user/$', views.create_user, name='create_user'),
]