from django.db import models

from books.models import Book
from members.models import Member


class Transaction(models.Model):
    STATUS_CHOICES = [
        ("Issued", "Issued"),
        ("Returned", "Returned"),
    ]
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Issued")

    def __str__(self):
        return f"{self.member.name} - {self.book.title}"
