from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('Question', 'category', 'created_at', 'updated_at')
    list_filter = ('category',)
    search_fields = ('Question', 'Answer')