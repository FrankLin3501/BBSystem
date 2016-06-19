# -*- coding: utf8 -*-

from __future__ import unicode_literals
from django.db import models

class User(models.Model):
	#UID = models.AutoField(primary_key=True)
	nickname = models.CharField(max_length=20, default=u"NONAME")
	password = models.CharField(max_length=10)

	def __unicode__(self):
		return self.nickname

class Article(models.Model):
	#AID = models.AutoField(primary_key=True)
	title = models.TextField(max_length=30, default=u"NO_TITLE")
	context = models.TextField(default=u"Nothing here...")
	postdate = models.DateField(auto_now_add=True)
	editdate = models.DateField(auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __unicode__(self):
		return self.title

class Message(models.Model):
	message = models.TextField()
	postdate = models.DateField(auto_now_add=True)
	article = models.ForeignKey(Article, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.message
