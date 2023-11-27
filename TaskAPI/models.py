from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):

    priority  = (
    ("LOW", "low"),
    ("NORMAL", "normal"),
    ("HIGH", "high"), )

    SelectProject  = (
    ("ANDELA", "andela"),
    ("TEK-EXPERTS", "tek-experts"),
    ("UDEMY", "udemy"), )

    Assignee = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, default='')
    description = models.TextField(null=True, blank=True, default='')
    priority =models.TextField(choices=priority, null=True, blank=True, default='')
    createTask =models.DateField(auto_now_add=True)
    endTask =models.DateField(auto_now_add=True)
    UploadFile = models.FileField(null=True)
    # Assignee = models.TextField(null=True, blank=True,default='')
    projects = models.CharField(max_length=50, choices= SelectProject, default='')

    def __str__(self):
        return self.title
    

    