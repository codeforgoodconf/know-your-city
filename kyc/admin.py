from django.contrib import admin

from .models.story import Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        # 'place',
        'date',
        'day_is_relevant',
        'month_is_relevant',
        'end_date',
        'end_day_is_relevant',
        'end_month_is_relevant',
        'summary',
        # 'media',
        'body',
        'references',
    ]
