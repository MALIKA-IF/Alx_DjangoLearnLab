from bookshelf.models import Book

books = Book.title("Nineteen Eighty-Four")
books.save()