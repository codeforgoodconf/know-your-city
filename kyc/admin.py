from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models.story import Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['title',
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
                    'references'
                    ]
