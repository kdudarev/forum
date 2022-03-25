from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import TopicForm, CommentForm
from .models import Topic


def index(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'forums/index.html', context)


@login_required
def topic(request, topic_id, slug):
    topic = Topic.objects.get(id=topic_id, slug=slug)
    context = {'topic': topic}
    return render(request, 'forums/topic.html', context)


@login_required
def add_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('forums:index')
    context = {'form': form}
    return render(request, 'forums/add_topic.html', context)


@login_required
def edit_topic(request, topic_id, slug):
    topic = Topic.objects.get(id=topic_id, slug=slug)
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = TopicForm(instance=topic)
    else:
        form = TopicForm(instance=topic, data=request.POST)
        form.save()
        return redirect(topic.get_absolute_url())
    context = {'topic': topic, 'form': form}
    return render(request, 'forums/edit_topic.html', context)


@login_required
def add_comment(request, topic_id, slug):
    topic = Topic.objects.get(id=topic_id, slug=slug)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        new_comment = form.save(commit=False)
        new_comment.owner = request.user
        new_comment.topic_id = topic.id
        new_comment.save()
        return redirect(topic.get_absolute_url())
    context = {'topic': topic, 'form': form}
    return render(request, 'forums/add_comment.html', context)
