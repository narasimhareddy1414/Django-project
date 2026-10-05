from django.db import models


class Note(models.Model):
    CATEGORY_CHOICES = [
        ('Python', 'Python'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('JavaScript', 'JavaScript'),
    ]

    Question = models.CharField(max_length=200)
    Answer = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Question