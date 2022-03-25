from django.urls import path

from . import views


app_name = 'forums'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:topic_id>/<slug:slug>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('edit_topic/<int:topic_id>/<slug:slug>/',
         views.edit_topic, name='edit_topic'),
]
