from django.urls import path

from . import views

urlpatterns = [
    path('', views.polls, name='polls'),
    path('create/', views.create, name='create'),
    path('results/', views.results, name='results'),
    path('vote/', views.vote, name='vote'),
]
