from bookshelf.models import Book

books = Book.objects.filter(title = "1984")
books.update(title = "Nineteen Eighty-Four")
books.save()