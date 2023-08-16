from django.urls import path
from .views import *

urlpatterns = [
    path('create_author/', create_author, name='create_author'),
    path('create_post/', create_post, name='create_post'),
    path('create_comment/', create_comment, name='create_comment'),
    path('search/', search, name='search'),]