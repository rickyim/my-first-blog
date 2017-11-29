# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 10:54:46 2017

@author: ricky
"""

from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^register$', views.UserFormView.as_view(), name = 'register'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^login$', auth_views.login, {'template_name': 'submission/login.html'}, name='login'),
]