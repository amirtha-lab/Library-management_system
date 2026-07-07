from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title
