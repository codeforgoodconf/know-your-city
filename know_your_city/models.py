from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200, required=True)
    description = models.TextField(required=True)
    # TODO: allow multiple media uploads
    media = models.FilePathField()

class Neighborhood(Category):
    # TODO: geodjango for shape file?
    location = models.FilePathField()

class Theme(Category):
    pass

class Era(Category):
    start_year = models.DateTimeField(blank=True, null=True)
    end_year = models.DateTimeField(blank=True, null=True)

# class Story(models.Model):
#     category = models.ManyToManyField()
#     author = models.ForeignKey(related_name='stories')
#
# class Author(models.Model):
#