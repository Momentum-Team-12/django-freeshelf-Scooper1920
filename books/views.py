from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .models import Category
from .models import Favorite
from .forms import FavoriteForm

def list_books(request):
    books=Book.objects.all()

    return render(request, "books/list_books.html",
                    {"books":books})


def book_detail(request,pk):
    form=FavoriteForm()
    book = Book.objects.get(pk=pk)
    context = {
        'book':book,
        'form':form
    }
    return render(request, 'books/book_detail.html',context)


def books_by_category(request,slug):
    category=Category.objects.get(slug=slug)
    books=Book.objects.filter(category=category)


    return render(request,'books/books_by_category.html',{"books":books, "category":category} )

#favorite view corresponds to to add album from django music
def add_favorite(request,pk):
#user does not need to be an argument because user is attached to the request.
    if request.method == 'POST':
        book= get_object_or_404(Book,pk=pk)
        user=request.user
        form = FavoriteForm(data=request.POST)
        if form.is_valid():
            favorite = form.save(commit=False)
            favorite.book=book
            favorite.user=user
            favorite.save()
            return redirect(to='book_detail',pk=pk)


def books_by_favorite(request):
     favorites=Favorite.objects.filter(user=request.user)
#.get is for one .filter is for many
#literally saying get the favorites for the specific user
     return render(request, 'books/books_by_favorite.html', {"favorites":favorites} )