from django.shortcuts import render, get_object_or_404, redirect
from .models import Note


def index(request):
    return render(request, 'index.html')


def all_notes(request):
    notes = Note.objects.all().order_by('-created_at')

    return render(request, 'notes.html', {
        'notes': notes
    })


def category_notes(request, category):
    notes = Note.objects.filter(
        category=category
    ).order_by('-created_at')

    return render(request, 'category.html', {
        'notes': notes,
        'category': category
    })


def add_note(request):

    if request.method == 'POST':

        question = request.POST.get('Question')
        answer = request.POST.get('Answer')
        category = request.POST.get('category')

        Note.objects.create(
            Question=question,
            Answer=answer,
            category=category
        )

        return redirect('all_notes')

    return render(request, 'add_note.html')


def note_detail(request, id):

    note = get_object_or_404(Note, id=id)

    return render(request, 'detail.html', {
        'note': note
    })


def update_note(request, id):

    note = get_object_or_404(Note, id=id)

    if request.method == 'POST':

        note.Question = request.POST.get('Question')
        note.Answer = request.POST.get('Answer')
        note.category = request.POST.get('category')

        note.save()

        return redirect('note_detail', id=note.id)

    return render(request, 'update_note.html', {
        'note': note
    })


def delete_note(request, id):

    note = get_object_or_404(Note, id=id)

    if request.method == 'POST':
        note.delete()

        return redirect('all_notes')

    return redirect('all_notes')