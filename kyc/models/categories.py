from django.db import models
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200, required=True)
    slug = models.SlugField(null=True, blank=True, editable=False, unique=True)
    description = models.TextField(blank=False, null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Neighborhood(Category):
    # TODO: geodjango for shape file?
    location = models.FilePathField()


class Theme(Category):
    pass


class Era(Category):
    start_year = models.DateTimeField(blank=True, null=True)
    end_year = models.DateTimeField(blank=True, null=True)


# class Story(models.Model):
#
#     def save(self, *args, **kwargs):
#         '''
#         save the created_date field, only when being created
#         save the modified field anytime it's saved
#         '''
#
#         super().save(*args, **kwargs)
#     # author = models.ForeignKey(related_name='stories')
#
