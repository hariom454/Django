"""Movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (home_view, movieFormView,actorFormView, producerFormView,
	producerDetailView, movie_detail,movie_edit,producer_edit,actor_detail,
	actor_edit,)
urlpatterns = [
    path('', home_view, name = 'home'),
    path('newmovie/', movieFormView, name = 'new_movie'),
    path('newactor/', actorFormView, name = 'new_actor'),
    path('newproducer/', producerFormView, name = 'new_producer'),
    path('producer/<int:my_id>/', producerDetailView, name = 'producer-detail'),
    path('movie/<int:mv_id>/', movie_detail, name = 'movie-detail'),
    path('movie/<int:my_id>/edit/', movie_edit, name = 'movie-edit'),
    path('producer/<int:my_id>/edit/', producer_edit, name = 'producer-edit'),
    path('actor/<int:my_id>/',actor_detail, name = 'actor-detail'),
    path('actor/<int:my_id>/edit/', actor_edit, name='actor-edit'),

]
