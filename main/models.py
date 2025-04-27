# main/models.py
from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    board = models.ForeignKey(Board, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    author_name = models.CharField(max_length=50, default="Anon")
    image_data = models.BinaryField(null=True, blank=True)  # 👈 храним файл в базе
    image_mime = models.CharField(max_length=50, null=True, blank=True)  # 👈 тип файла (например image/png)

    def __str__(self):
        return f"{self.title} (#{self.id})"
