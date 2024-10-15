

from django.shortcuts import redirect, render
from django.utils.text import slugify
from notes.models import Note

from .forms import AddNoteForm

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



def add_note(request):
    if request.method == 'POST':
        if (form := AddNoteForm(request.POST)).is_valid():


            post = form.save(commit=False)


            post.slug = slugify(post.title)


            post.save()


            return redirect('notes:home')


    else:
        form = AddNoteForm()


    return render(request, 'notes/add_note.html', dict(form=form))