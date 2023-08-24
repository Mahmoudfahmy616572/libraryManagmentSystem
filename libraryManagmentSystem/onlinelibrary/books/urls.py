
from django.urls import path , include
from books.views import index , show ,editBook, index_borrow
urlpatterns = [
            path('',index ,name='books.index'),
            path('borrow',index_borrow,name='borrow.index'),
            path('<int:id>', show, name='books.show'),
            path('<int:id>/edit',editBook,name= 'books.edit'),

]