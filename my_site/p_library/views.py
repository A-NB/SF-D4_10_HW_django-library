from django.shortcuts import render
from p_library.models import Book, PublishingHouse
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

def index(request):
    template = loader.get_template('index.html')    
    welcome_dict = {
        "welcome_phrase": "Добро пожаловать в мою библиотеку!",
    }
    return HttpResponse(template.render(welcome_dict, request,)) 

def make_range(request):
    range_ = range(1, 101)
    return HttpResponse(range_)

def books(request):
    template = loader.get_template('books.html')
    books = Book.objects.all()    
    biblio_data = {
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request,)) 

def publishers(request):
    template = loader.get_template('publishers.html')
    pub_houses = PublishingHouse.objects.all()
    books_counter = Book.objects.count()
    pub_houses_data = {
        "title": "Книжные издательства:",
        "pub_houses": pub_houses,
        "books_counter": books_counter,
    }
    return HttpResponse(template.render(pub_houses_data, request,)) 

def copy_count_change(request, action):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/books/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/books/')
            if action == '+':
                book.copy_count += 1
            elif action == '-':
                if book.copy_count < 1:
                    book.copy_count = 0
                else:
                    book.copy_count -= 1
            book.save()
        return redirect('/books/')
    else:
        return redirect('/books/')

def book_increment(request):
    return(copy_count_change(request, '+'))

def book_decrement(request):
    return(copy_count_change(request, '-'))