from django.shortcuts import render, get_object_or_404
from . import models


def books(request):
    """
        Вывод неполной информации
    """
    book = models.Book.objects.all()
    return render(request, 'books.html', {'book':book})


def book_full_view(request, id):
    """
        Вывод полной информации по id
    """
    book_id = get_object_or_404(models.Book, id=id)
    return render(request, 'books_detail.html', {'books_id': book_id})