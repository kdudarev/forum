from django.shortcuts import render

from .models import Topic


def index(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'forums/index.html', context)


def topic(request, topic_id, slug):
    topic = Topic.objects.get(id=topic_id, slug=slug)
    context = {'topic': topic}
    return render(request, 'forums/topic.html', context)
