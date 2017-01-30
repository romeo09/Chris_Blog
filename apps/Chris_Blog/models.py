from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import datetime, json, re, bcrypt

json.JSONEncoder.default = lambda self,obj: (obj.isoformat() if isinstance(obj, datetime.datetime) else None)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-_]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class CommentManager(models.Manager):
    def CommentData(self, data):
        errors = []
        now = datetime.datetime.now()

        if len(data.POST['name']) < 2:
            errors.append('Please make your NAME more than 2 characters')
        if len(data.POST['comment']) == ' ':
            errors.append('Your Comment message is empty!')
        # if not EMAIL_REGEX.match(data.POST['email']):
        #     errors.append('The EMAIL you used is not a VALID email address')
        return errors

    def ValidComment(self, data):
        errors = self.CommentData(data)

        if len(errors) > 0:
            return(False, errors)

            comment = self.create(comment = data.POST['comment'], name = data.POST['name'])

            return(True, newComment)

class Blog(models.Model):
    title = models.CharField(max_length = 50)
    blog = models.TextField()
    author = models.CharField(max_length = 100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Comment(models.Model):
    # blog = models.ForeignKey(Blog)
    comment = models.TextField()
    name = models.CharField(max_length = 25)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = CommentManager()
