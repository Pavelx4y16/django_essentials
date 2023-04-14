from django.urls import path

from notes import views

urlpatterns = [
    path('notes', views.NoteList.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NoteDetail.as_view(), name="note.details"),
    path('notes/<int:pk>/edit', views.EditNote.as_view(), name="note.edit"),
    path('notes/<int:pk>/delete', views.DeleteNote.as_view(), name="note.delete"),
    path('notes/new', views.CreateNote.as_view(), name="note.new"),
]
