from django.db import models

# Create your models here.



class UserInfo(models.Model):
    describe = models.CharField(max_length=1000)
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    loginTimes = models.IntegerField(default=0)

    def __str__(self):
        return self.userName

class Passage(models.Model):
    author = models.ForeignKey(UserInfo)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    creationTime = models.DateTimeField(auto_now_add=True)
    changeTime = models.DateTimeField(auto_now=True)
    readTimes = models.IntegerField(default=0)
    goodTimes = models.IntegerField(default=0)
    badTimes = models.IntegerField(default=0)

    def __str__(self):
        return self.title



class Replies(models.Model):
    author = models.ForeignKey(UserInfo)
    content = models.CharField(max_length=500)
    passage = models.ForeignKey(Passage)
    replyTime = models.DateTimeField(auto_now_add=True)
    goodTime = models.IntegerField(default=0)

    def __str__(self):
        return self.passage
