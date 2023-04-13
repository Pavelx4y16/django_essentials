from django.urls import path

from notes import views

urlpatterns = [
    path('notes', views.list_notes),
    path('notes/<int:pk>', views.note_details)
]
