from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'), #URL mapper ex) <uuid:ppk> : special formatted string to capture book id, pk is the parameter to pass to view, we can also use regular expressions to express advanced path matching
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]
urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name = 'my-borrowed'),
]
urlpatterns += [
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
]
