# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from bbsystem.models import *
from django.template import Context, loader
from django.utils.html import escape

def index(request):
	response = u''
	response1 = u""
	list = Article.objects.all()
	for var in list:
		response1 += u'<h1 class="tr">'
		response1 += u'<a class="td td_title" href="../article/{0}/">{1}</a>'.format(var.id, var.title)
		response1 += u'<a class="td td_author" href="../author/{0}">{0}</a>'.format(var.user.nickname)
		response1 += u'<div class="td td_postdate">{0}</div>'.format(var.postdate) + '</h1>'
	response = response + response1
	print response
	return render(request, 'index.html', [{'dbList', response}], content_type="text/html; charset=utf8")

def article(request, id):
	article = Article.objects.get(id=int(id))
	return render(request, 'article.html', [{'article', article}])
