from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
path('',views.HomePageView,name='home'),
path('board/<int:board_id>/new',views.boards_topics,name='boards_topics')
]
