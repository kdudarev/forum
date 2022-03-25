from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from .forms import TopicForm, CommentForm
from .models import Topic


def index(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'forums/index.html', context)


def topic(request, topic_id, slug):
    topic = Topic.objects.get(id=topic_id, slug=slug)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.owner = request.user
            form.topic = topic
            form.save()
            return redirect(topic.get_absolute_url())
    context = {'topic': topic, 'form': form}
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
        if form.is_valid():
            form.save()
            return redirect(topic.get_absolute_url())
    context = {'topic': topic, 'form': form}
    return render(request, 'forums/edit_topic.html', context)


class DeleteTopicView(DeleteView):
    model = Topic
    success_url = reverse_lazy('forums:index')
    template_name = 'forums/delete_topic.html'
