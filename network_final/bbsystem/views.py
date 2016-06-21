# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from bbsystem.models import *
from django.template import Context, loader
from django.utils.html import escape
from django.core import serializers


def index(request):
	print request.get_full_path()
	response = u''
	response1 = u''
	a = Article.objects.all()
	if a.count() == 0:
		error(request)
	content = {
		'articles': a
	}
	return render(request, 'index.html', content, content_type="text/html; charset=utf8")

def article(request):
	pk = request.GET['id']
	a = Article.objects.filter(id=int(pk))
	if a.count() == 0:
		return error(request)
	messages = Message.objects.filter(article=a[0])
	a = a[0]
	content = {
		'article': a,
		'messages': messages
	}
	return render(request, 'article.html', content, content_type="text/html; charset=utf8")

def error(request):
	
	return HttpResponse(u'404 Not Found')
