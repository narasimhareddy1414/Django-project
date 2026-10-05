from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('notes/', views.all_notes, name='all_notes'),

    path('add/', views.add_note, name='add_note'),

    path('note/<int:id>/', views.note_detail, name='note_detail'),

    path('note/<int:id>/update/', views.update_note, name='update_note'),

    path('note/<int:id>/delete/', views.delete_note, name='delete_note'),

    path(
        'category/<str:category>/',
        views.category_notes,
        name='category_notes'
    ),
]