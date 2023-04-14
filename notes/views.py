from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView

from notes.models import Notes


class NoteList(ListView):
    model = Notes
    template_name = 'notes/list_notes.html'
    context_object_name = 'notes'


class NoteDetail(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/note_details.html'
