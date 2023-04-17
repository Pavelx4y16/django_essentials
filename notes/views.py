from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class NoteList(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'notes/list_notes.html'
    context_object_name = 'notes'
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()


class NoteDetail(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/note_details.html'
