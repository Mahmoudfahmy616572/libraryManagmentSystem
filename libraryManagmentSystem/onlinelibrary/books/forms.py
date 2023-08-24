from django import  forms
from books.models import Book

class BorrowBookFrom(forms.ModelForm):
    borrower_name = forms.CharField(max_length=100)
