from django.shortcuts import render, redirect

from .forms import TopicForm
from .models import Topic


def index(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'forums/index.html', context)


def topic(request, topic_id, slug):
    topic = Topic.objects.get(id=topic_id, slug=slug)
    context = {'topic': topic}
    return render(request, 'forums/topic.html', context)


def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('forums:index')
    context = {'form': form}
    return render(request, 'forums/new_topic.html', context)
