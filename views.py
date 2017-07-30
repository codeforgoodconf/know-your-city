from django.views import View
from django.shortcuts import render
from .models import Story

# Create your views here.
total_stories = Story.objects.count()

class StoryList(View):
    template = 'base.html'

    def get(self, request, slug):
        # get all stories from the selected 'category'
        stories = Story.objects.filter(categories__slug=slug)
        context = {
            'stories': stories
        }

        # return response = json ?
        render(request, self.template, context)