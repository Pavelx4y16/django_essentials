from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from notes.forms import NotesForm
from notes.models import Notes


class DeleteNote(DeleteView):
    model = Notes
    template_name = "notes/delete_note.html"
    success_url = "/notes"
    context_object_name = 'note'


class EditNote(UpdateView):
    model = Notes
    template_name = "notes/note_form.html"
    form_class = NotesForm
    success_url = '/notes'


class CreateNote(CreateView):
    model = Notes
    template_name = "notes/note_form.html"
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
