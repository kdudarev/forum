from django.urls import path

from . import views


app_name = 'forums'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:topic_id>/<slug:slug>/', views.topic, name='topic'),
]
