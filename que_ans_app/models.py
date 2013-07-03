from django.db import models
from django.contrib import admin
# Create your models here.


class Question(models.Model):
    que_owner = models.CharField(max_length=20)
    que_description = models.TextField()
    que_publish_time = models.DateField()

    def __unicode__(self):
        return self.que_description

    class Admin:
        pass


class Answer(models.Model):
    ans_description = models.TextField()
    ans_publish_time = models.DateField()
    question = models.ForeignKey(Question)

    def __unicode__(self):
        """


        :return:
        """
        return self.ans_description


class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_tile = models.CharField(max_length=100)
    blog_content = models.TextField()
    blog_owner = models.IntegerField()
    blog_publish_time = models.DateTimeField()
    blog_sort = models.CharField(blank=True, max_length=50)
    blog1 = models.CharField(blank=True, max_length=50)
    blog2 = models.CharField(blank=True, max_length=50)
    blog3 = models.CharField(blank=True, max_length=50)
    blog4 = models.CharField(blank=True, max_length=50)


class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=50)
    user1 = models.CharField(blank=True, max_length=50)
    user2 = models.CharField(blank=True, max_length=50)
    user3 = models.CharField(blank=True, max_length=50)
    user4 = models.CharField(blank=True, max_length=50)
    user5 = models.CharField(blank=True, max_length=50)
    user6 = models.CharField(blank=True, max_length=50)
    user7 = models.CharField(blank=True, max_length=50)
    user8 = models.CharField(blank=True, max_length=50)
    user9 = models.CharField(blank=True, max_length=50)

    class Admin:
        pass


admin.site.register(Question)
admin.site.register(Answer)
