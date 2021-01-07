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

from django.views import generic
class BookListView(generic.ListView):
    model = Book
    '''
    get_query_set() methd override-> change record's list
    def get_queryset(self):
        return Book.objects.filter(title__icontains='Data')[:5] #Get 5 books containing the title Data

    or we could override get_context_data() -> pass extra context parameters at template
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_contect_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context
    #follows certain patterns 1. Bring original context from super class 2.Add new context info 3. Return updated context
    '''
    paginate_by = 4    #pagination : if you get 10 or more records, view will start pagination, we can access page2 by using URL = /catalog/books/?page=2
class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4

class AuthorDetailView(generic.DetailView):
    model = Author
