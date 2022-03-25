from django.urls import path

from . import views
from .views import DeleteTopicView, HomeView

app_name = 'forums'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:topic_id>/<slug:slug>/',
         views.topic_detail, name='topic_detail'),
    path('add_topic/', views.add_topic, name='add_topic'),
    path('edit_topic/<int:topic_id>/<slug:slug>/',
         views.edit_topic, name='edit_topic'),
    path('delete_topic/<int:topic_id>/<slug:slug>/',
         DeleteTopicView.as_view(), name='delete_topic'),
    path('like_topic/<int:topic_id>/<slug:slug>/',
         views.like_topic, name='like_topic'),
]
