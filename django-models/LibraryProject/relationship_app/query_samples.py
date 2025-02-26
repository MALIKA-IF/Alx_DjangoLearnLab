from .models import Author, Book, Librarian, Library

#Query all books by a specific author
author=Author.objects.create(name="Author_name")
books_author=author.books.all()
   
#List all books in a library. 
lib=Library.objects.create(name="library_name")
books_library = lib.library.all()   

#Retrieve the librarian for a library

lib2=Librarian.objects.create(name="Librarian_name")    
lib2.librarian.all()