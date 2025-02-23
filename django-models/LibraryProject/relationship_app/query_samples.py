from .models import Author, Book, Librarian, Library

author=Author.objects.get(name="Author_name")
books_author=author.books.all()
   
library=Library.objects.get(name="library_name")
books_library = library.books.all()   


book=Book.objects.get(title="Book_title")
library=book.library
librarian=library.librarian
print(librarian.name)    