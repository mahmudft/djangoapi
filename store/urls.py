from django.urls import path
from store import views

urlpatterns = [
    #path('', views.index),
    path('songs/', views.song_list),
    path('songs/<int:id>/', views.song_by_id),
]
