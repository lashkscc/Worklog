from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Status(models.Model):
    statusName=models.CharField(max_length=255)
    statusDescription=models.CharField(max_length=255)
    statusPosition=models.IntegerField

    def __str__(self):
        return self.statusName

    class Meta:
        db_table='status'
        verbose_name_plural='statuses'

class Task(models.Model):
    taskName=models.CharField(max_length=255)
    taskDescription=models.CharField(max_length=255)
    taskUserCreated= models.ForeignKey(User, on_delete=models.CASCADE)
    taskDateCreated=models.DateField()
    taskDeadline=models.DateField(blank=True)
    taskStatus=models.ForeignKey(Status, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.taskName
    
    class Meta:
        db_table='task'


class TaskComment(models.Model):
    taskid=models.ForeignKey(Task, on_delete=models.CASCADE)
    taskCommentDescription=models.CharField(max_length=255)
    taskUserCreated= models.ForeignKey(User, on_delete=models.CASCADE)
    taskDateCreated=models.DateField()
    def __str__(self):
        return self.taskid.taskName
    
    class Meta:
        db_table='taskcomment'