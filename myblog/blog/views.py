# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

blog_index = {'hello': 'HELLO BLOG'}

def index(request):
  return render(request, 'blog/index.html', blog_index)
