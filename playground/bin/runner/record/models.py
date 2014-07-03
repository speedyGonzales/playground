#the django libs
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Record(models.Model):
    user = models.ForeignKey(User)
    description=models.TextField()
    distance=models.IntegerField()
    reg_date=models.DateTimeField(auto_now_add=True, auto_now=False)


def __unicode__(self):
    return unicode(self.description)
