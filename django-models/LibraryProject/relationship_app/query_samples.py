from .models import Author, Book, Librarian, Library

author = Author.objects.get(name="Author Name")

books_author = author.books.all()
   
library = Library.objects.get(name="name_Library")
books_library = library.books.all()   

book = Book.objects.get(title="Book_title")

library = book.library
librarian = library.librarian
print(librarian.name)    