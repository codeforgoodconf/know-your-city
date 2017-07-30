from django.db import models
from django.utils import timezone


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
    story = models.ForeignKey('Story', related_name='story_media')


class CategoryMedia(Media):
    category = models.ForeignKey('Category', related_name='media_files')
