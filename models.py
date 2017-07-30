from django.db import models
from django.utils import timezone
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

class Story(models.Model):
    categories = models.ManyToManyField(Category, related_name='categories')
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        '''
        save the created_date field, only when being created
        save the modified field anytime it's saved
        '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()

        super().save(*args, **kwargs)
    # author = models.ForeignKey(related_name='stories')


def handler(instance, filename):
    # TODO: complete filepath
    filepath = f'{filename}'
    return filepath


class Media(models.Model):
    '''
    Used to upload multiple media objects to an object.
    '''
    file = models.FileField(upload_to=handler)
    created = models.DateTimeField(editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        '''
        Populate the created_date field, only when being created
        '''
        if not self.id:
            self.created = timezone.now()

        # TODO: extension = self.file.path.split('.')[-1]
        # if extension in extensions ...

        super().save(*args, **kwargs)


class StoryMedia(Media):
    story = models.ForeignKey(Story, related_name='story_media')

class CategoryMedia(Media):
    category = models.ForeignKey(Category, related_name='media_files')
