from django.db import models
from django.utils import timezone


class Story(models.Model):
    title = models.CharField(max_length=256, unique=True)
    categories = models.ManyToManyField('Category', related_name='categories')
    # place = models.ForeignKey(Place)

    # if this story takes place over a range of time, the date field will act
    # as a start date
    date = models.DateField()
    # if the story started (and possibly ended) on an exact day
    day_is_relevant = models.BooleanField(default=True)
    # if the story started (and possibly ended on an exact month
    month_is_relevant = models.BooleanField(default=True)

    end_date = models.DateField(null=True)
    # if the story ended on an exact day
    end_day_is_relevant = models.NullBooleanField(null=True)
    # if the story ended on an exact month
    end_month_is_relevant = models.NullBooleanField(null=True)

    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)

    summary = models.CharField(max_length=256)

    # media

    body = models.CharField(max_length=65536)

    references = models.CharField(max_length=512)

    # author = models.ForeignKey(Author)
    # theme = models.ForeignKey(Theme)

    def save(self, commit=True):
        story = super().save(commit=False)
        if story.end_date is None:
            story.end_day_is_relevant = None
            story.end_month_is_relevant = None
        if commit:
            story.save()
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()

        return story
