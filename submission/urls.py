# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 10:54:46 2017

@author: ricky
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]