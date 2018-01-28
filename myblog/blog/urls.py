# -*- coding: utf-8 -*-
from django.conf.urls import url
import blog.views as bv
# from . import views
urlpatterns = [
    url(r'^$', bv.index),
    url(r'^index/$', bv.index), #特别注意index后面的 /
]