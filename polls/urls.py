from django.urls import path

from . import views

urlpatterns = [
    path('', views.poll, name='polls'),
    path('create/', views.create, name='create'),
    path('results/<poll_id>/', views.results, name='results'),
    path('<poll_id>/', views.vote, name='vote'),
    path('success/<poll_id>/', views.success, name='success'),
    ]
