from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from .models import Record

# Create your tests here.
class SimpleTest(TestCase):
    def setUp(self):
        user = User.objects.create_user("ak", "ak@abc.org", "pwd")
        user.save()
        record= Record.objects.create(description="test", user=u, distance=10)
        record.save()
