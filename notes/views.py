from django.shortcuts import render

from notes.models import Notes


def list_notes(request):
    all_notes = Notes.objects.all()
    return render(request, template_name='notes/list_notes.html', context={'notes': all_notes})


def note_details(request, pk):
    note = Notes.objects.get(pk=pk)
    return render(request, template_name='notes/note_details.html', context={'note': note})
