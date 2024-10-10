
from django.shortcuts import render
from notes.models import Note


def home(request):
    num_notes = Note.objects.count()
    notes = Note.objects.all()
    return render(
        request,
        'home.html',
        {'num_notes': num_notes, 'notes': notes},
    )


def note_detail(request, note_slug: str):
    note = Note.objects.get(slug=note_slug)
    return render(request, 'notes/detail.html', dict(note=note))
