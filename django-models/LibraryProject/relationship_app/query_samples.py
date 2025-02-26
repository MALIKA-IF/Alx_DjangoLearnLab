from .models import Author, Book, Librarian, Library

#List all books in a library. 
lib=Library.objects.get(name='library_name')
lib.library.all()   

#Query all books by a specific author
author=Author.objects.create(name='Author_name')
author.books.all()
   

#Retrieve the librarian for a library

lib2=Librarian.objects.create(name='Librarian_name')    
lib2.librarian.all()