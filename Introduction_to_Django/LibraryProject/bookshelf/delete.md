from bookshelf.models import Book

books = Book.objects.get()
books.delete()
books.objects.all()