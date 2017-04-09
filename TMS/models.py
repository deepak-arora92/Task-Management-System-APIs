from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tasks(models.Model):
    task_id = models.AutoField(primary_key = True)
    task_desc = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add = True)

class StudentTasks(models.Model):
    user = models.ForeignKey(User)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    status =  models.CharField(max_length=20, default = 'to-do')
    is_approved = models.NullBooleanField(null=True)

