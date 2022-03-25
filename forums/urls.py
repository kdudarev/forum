from django.urls import path

from . import views


app_name = 'forums'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:topic_id>/<slug:slug>/', views.topic, name='topic'),
    path('add_topic/', views.add_topic, name='add_topic'),
    path('edit_topic/<int:topic_id>/<slug:slug>/',
         views.edit_topic, name='edit_topic'),
]
