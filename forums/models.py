from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        ordering = ['-date_added']


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    forum_post = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.owner} - {self.forum_post}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-date_added']
