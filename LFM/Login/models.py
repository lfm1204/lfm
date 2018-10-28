from django.db import models

# Create your models here.




class UserInfo(models.Model):
    describe = models.CharField(max_length=1000, default='介绍')
    userName = models.CharField(max_length=100, default='用户名')
    password = models.CharField(max_length=100, default='密码')
    question = models.CharField(max_length=100, default='密保问题')
    answer = models.CharField(max_length=100, default='密保答案')

class Passage(models.Model):
    author = models.ForeignKey(UserInfo)
    title = models.CharField(max_length=100, default='标题')
    content = models.CharField(max_length=10000, default='内容')
    creationTime = models.DateTimeField

class Replies(models.Model):
    author = models.ForeignKey(UserInfo)
    content = models.CharField(max_length=500, default='回复内容')
    passage = models.ForeignKey(Passage)
    replyTime = models.DateTimeField

