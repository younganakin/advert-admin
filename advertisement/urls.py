from django.urls import path

from . import views

app_name = 'advertisement'

urlpatterns = [
    path('', views.index, name='index'),
]