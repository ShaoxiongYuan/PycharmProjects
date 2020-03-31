from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Book


# Create your views here.
def book(request):
    books = Book.objects.filter(is_active=True)
    return render(request, 'bookstore/book.html', locals())


def update(request, id):
    if request.method == 'GET':
        try:
            book = Book.objects.get(id=int(id), is_active=True)
        except Exception as e:
            print(e)
            return HttpResponse("No book...")
        else:
            return render(request, 'bookstore/update_book.html', locals())
    elif request.method == 'POST':
        price = request.POST.get('price')
        market_price = request.POST.get('market_price')

        if not price or not market_price:
            return HttpResponse("Please fill in the blanks")

        book = Book.objects.get(id=int(id))
        if float(price) != book.price or float(market_price) != book.market_price:
            book.price = price
            book.market_price = market_price
            book.save()

        return HttpResponseRedirect('/bookstore/book')


def delete(request, id):
    try:
        book = Book.objects.get(id=int(id), is_active=True)
    except Exception as e:
        print(e)
        return HttpResponse("No book...")
    else:
        book.is_active = False
        book.save()
        return HttpResponseRedirect(reverse('all_book'))


def add(request):
    if request.method == 'GET':
        return render(request, 'bookstore/add_book.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        pub = request.POST.get('pub')
        price = request.POST.get('price')
        market_price = request.POST.get('market_price')
        books = Book.objects.all()
        for book in books:
            if title == book.title:
                return HttpResponse('书籍已存在')
        Book.objects.create(title=title, pub=pub, price=price, market_price=market_price)
        return HttpResponseRedirect('/bookstore/book')
