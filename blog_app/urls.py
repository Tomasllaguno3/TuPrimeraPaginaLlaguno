from django.urls import path
from . import views

urlpatterns = [
    path('create_author/', views.create_author, name='create_author'),
    path('create_post/', views.create_post, name='create_post'),
    path('create_comment/', views.create_comment, name='create_comment'),
    path('search/', views.search, name='search'),]