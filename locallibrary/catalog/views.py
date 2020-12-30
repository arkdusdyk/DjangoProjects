from django.shortcuts import render

# Create your views here.
#View는 HTTP요청을 처리하고, DB에서 요청된 데이터를 가져오고, HTML 템플릿으로 data를 HTML page에 rendering, HTML을 HTTP 응답으로 반해 사용자들에게 보여줌
from catalog.models import Book, Author, BookInstance, Genre
def index(request):
    #View function for homepage of site
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    #generating count of main objects..

    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()
    #available books

    num_authors = Author.objects.count()
    #'all()' is implied by default

    context = {
        'num_books': num_books,
        'num_instances' : num_instances,
        'num_instances_available' : num_instances_available,
        'num_authors' : num_authors,
    }
    return render(request, 'index.html',context=context)
    #rendering HTML template index.html with data in context variable
