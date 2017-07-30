from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=256, unique=True)
    # place = models.ForeignKey(Place)

    date = models.DateField()
    end_date = models.DateField(null=True)

    summary = models.CharField()

    # media

    body = models.CharField()

    references = models.CharField()

    # author = ForiegnKey(Author)