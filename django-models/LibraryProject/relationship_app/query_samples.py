from relationship_app.models import Author, Library, Book, Librarian


#List all books in a library. 
Library.objects.get(name='library_name')
#lib.library.all()   

#Query all books by a specific author
author=Author.objects.get(name='Author_name')
author.books.all()
   

#Retrieve the librarian for a library

lib2=Librarian.objects.get(name='Librarian_name')    
lib2.librarian.all()