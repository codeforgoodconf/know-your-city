from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=256, unique=True)
    # place = models.ForeignKey(Place)

    year = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField(null=True)
    day = models.PositiveSmallIntegerField(null=True)

    summary = models.CharField()
