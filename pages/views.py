from django.shortcuts import render
from django.http import HttpResponse
from pages.models import *


def index(request):
    modules = Module.objects.all()
    topics = Topic.objects.all()
    subtopics = Subtopic.objects.all()
    context = {'modules': modules, 'topics': topics, 'subtopics': subtopics}
    return render(request, 'pages/index.html', context)
