# -*- coding:utf-8 -*-
from django.db import models
from django.contrib import admin
# Create your models here.

class Category(models.Model):
    name = models.CharField(default = "指定なし", max_length=200, unique=True)
    class Meta:
        verbose_name = verbose_name_plural = "Categories"
    def __unicode__(self):
        return self.name


PRIORITY_CHOICES=(('N', 'now'), ('S', 'soon'), ('L', 'later'))
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    is_finished = models.BooleanField(default=False)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='L')
    cotegory = models.ForeignKey(Category)

    def __unicode__(self):
        return self.title[:10]+u'...'
admin.site.register(Category)
admin.site.register(Todo)
