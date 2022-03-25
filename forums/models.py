from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Topic(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=75, blank=True)
    likes = models.ManyToManyField(User, related_name='topic_likes')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forums:topic_detail', args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Topic, self).save(*args, **kwargs)

    def get_comment(self):
        return self.comment_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        ordering = ['-date_added']


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return f'{self.owner} - {self.topic}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-date_added']
