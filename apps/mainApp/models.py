from __future__ import unicode_literals
from ..loginAndReg.models import User
from django.db import models

class Wishlist(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User, related_name="wishes")
    creator = models.ForeignKey(User, related_name="created_wishes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
