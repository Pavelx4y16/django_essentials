from django.urls import path

from notes import views

urlpatterns = [
    path('list_notes', views.list_notes)
]
