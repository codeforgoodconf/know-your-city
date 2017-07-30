from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=256, unique=True)
    # place = models.ForeignKey(Place)

    date = models.DateField()  # if this story takes place over a range of time, the date field will act as a start date
    day_is_relevant = models.BooleanField(default=True)  # if the story started (and possibly ended) on an exact day
    month_is_relevant = models.BooleanField(default=True)  # if the story started (and possibly ended on an exact month

    end_date = models.DateField(null=True)
    end_day_is_relevant = models.NullBooleanField(null=True)  # if the story ended on an exact day
    end_month_is_relevant = models.NullBooleanField(null=True)  # if the story ended on an exact month


    summary = models.CharField()

    # media

    body = models.CharField()

    references = models.CharField()

    # author = models.ForeignKey(Author)
    # theme = models.ForeignKey(Theme)

    def save(self, commit=True):
        story = super().save(commit=False)
        if story.end_date is None:
            story.end_day_is_relevant = None
            story.end_month_is_relevant = None
        if commit:
            story.save()
        return story


