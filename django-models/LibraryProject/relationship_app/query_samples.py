from .models import Author, Book, Librarian, Library

books = Book.objects.get(Library='Library_name')
books.all()
   

for p in Library.objects.raw("SELECT books FROM Library "):
    print(p)    

for p in Librarian.objects.raw("DELETE name FROM Librarion WHERE Library=''"):
    print(p)       