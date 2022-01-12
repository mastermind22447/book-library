from django.http import HttpResponse
from .models import Book
from django.shortcuts import redirect, render
from django.template import loader
from .forms import BookForm
from django.db import models

from books import forms

def books_home(request):
    books = Book.objects.all()
    # print("--------------------------------------")
  
    # print("--------------------------------------")

    template = loader.get_template('books/index.html')
    context = {
        'books': books,
        'sajjad': 321321,
        'sina': "asdasd"
    }
    return HttpResponse(template.render(context, request))

    # return render(request, 'index.html')
    
    # return HttpResponse("book 1 prdffdsfsdfice is " + books[1].price + " ---- " + books[1].title)

def book_detail(request, book_id):

    book = Book.objects.get(pk=book_id)

    template = loader.get_template('books/details.html')
    context = {
        'book': book,
        'sajjad': 321321,
        'sina': "asdasd"
    }
    return HttpResponse(template.render(context, request))

def book_edit(request, book_id):
    book = Book.objects.get(pk=book_id)
    form = BookForm(instance=book)
    
    
    
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'books/edit.html', context)


def book_update(request, book_id):

    book = Book.objects.get(pk=book_id)
    # create a QueryDict of books that gets book objects from db based on their ID.
    
    print("Request: ", request.POST)

    # prints requested QueryDict of books objects.

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    
    # checks if method of request.POST is True, create a form based on BookForm in forms that contain book objects
    # and checkes if forms data is ok then saves data in db
            
    return redirect('book-home')

    # return to book-home url

def book_delete(request, book_id):

    Book.objects.filter(id=book_id).delete()
    print("--------------------------------------")

    return redirect('book-home')



def book_add(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        'form' : form
    }
    return render(request, 'books/add.html', context)


def book_insert(request):
    title = request.POST.get('title')
    price = request.POST.get('price')
    author = request.POST.get('author')
    kind = request.POST.get('kind')
    year = request.POST.get('year')
    
    
    book = Book()
    book.title = title
    book.price = price
    book.author = author
    book.kind = kind
    book.year = year
    
    book.save()
    
    
    print(f"title: {title} price: {price}")
    
    return redirect('book-home')
