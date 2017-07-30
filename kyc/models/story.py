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

    # author = ForeignKey(Author)