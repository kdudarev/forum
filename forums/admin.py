from django.contrib import admin

from forums.models import Topic, Comment


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added', 'owner', 'draft')
    list_display_links = ('title',)
    list_filter = ('owner',)
    search_fields = ('title',)
    list_editable = ('draft',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'date_added', 'topic')
