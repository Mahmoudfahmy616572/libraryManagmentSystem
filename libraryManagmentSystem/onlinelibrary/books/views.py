import datetime
from django.shortcuts import render , get_object_or_404, redirect
from books.models import Book
from django.views.generic import ListView






def index(request):
    book = Book.get_all_categorys()
    return render(request, 'books/index.html', context={"books":book})

def index_borrow(request):
    book = Book.get_all_categorys()
    return render(request, 'books/borrow_book.html', context={"books":book})

def show(request, id):
    book = Book.get_specific_category(id=id)
    return render(request, 'books/show.html', context={'books':book})



def editBook(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':

        if 'borrow' in request.POST:
            borrowed = True
        else:
            borrowed = False

        book.borrowed = borrowed
        book.save()
        print(book.borrowed)
        return redirect('books.index')


    return render(request,  'books/borrow.html', context={"book":Book})














