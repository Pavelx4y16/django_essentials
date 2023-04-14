from django.views.generic import ListView, DetailView, CreateView

from notes.forms import NotesForm
from notes.models import Notes


class CreateNote(CreateView):
    template_name = "notes/note_creation_form.html"
    form_class = NotesForm
    success_url = '/notes'


class NoteList(ListView):
    model = Notes
    template_name = 'notes/list_notes.html'
    context_object_name = 'notes'


class NoteDetail(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/note_details.html'
