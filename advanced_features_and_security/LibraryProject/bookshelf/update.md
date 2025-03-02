from bookshelf.models import Book

books = Book.objects.filter(book.title = "1984")
books.update(book.title = "Nineteen Eighty-Four")
books.save()