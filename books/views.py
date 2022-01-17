from re import search
from unicodedata import name
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
    
    
    print("Request: ", request.POST)

    
    form = BookForm(request.POST, instance=book)     
    if form.is_valid():
        form.save()
    
                
    return redirect('book-home')



def book_delete(request, book_id):

    Book.objects.filter(id=book_id).delete()
    print("--------------------------------------")

    return redirect('book-home')



def book_add(request, book_name):
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

def book_search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', False)
        books = Book.objects.filter(title__contains=searched)
        
        return render(request, 'books/search.html', {'searched' : searched ,'books': books})
    else:
        return render(request, 'books/search.html', {})
