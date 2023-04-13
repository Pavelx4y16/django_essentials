from django.shortcuts import render

from notes.models import Notes


def list_notes(request):
    all_notes = Notes.objects.all()
    return render(request, template_name='notes/list_notes.html', context={'notes': all_notes})
