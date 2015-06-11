
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Member(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    twitter = models.CharField(max_length=250, null=True, blank=True)
    facebook = models.CharField(max_length=250, null=True, blank=True)
    linkedn = models.CharField(max_length=250, null=True, blank=True)
    googleplus = models.CharField(max_length=250, null=True, blank=True)
    hakkinda = models.TextField(max_length=1000)
    bolum = models.CharField(max_length=50)
    sinif = models.IntegerField(default=0)
    points = models.PositiveIntegerField(default=0)
    points_counter = models.PositiveIntegerField(default=0)#how many peoples give vote
    active = models.BooleanField(default=True, editable=False)
    cdate = models.DateTimeField(auto_now_add=True)

class Document(models.Model):
    member = models.ForeignKey(Member, null=True, blank=True)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    def __unicode__(self):
        return self.docfile.name

class Permission(models.Model):
    document = models.ForeignKey(Document)
    member = models.ForeignKey(Member)