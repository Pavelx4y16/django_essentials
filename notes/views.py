from django.shortcuts import render
from django.http import Http404

from notes.models import Notes


def list_notes(request):
    all_notes = Notes.objects.all()
    return render(request, template_name='notes/list_notes.html', context={'notes': all_notes})


def note_details(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, template_name='notes/note_details.html', context={'note': note})
