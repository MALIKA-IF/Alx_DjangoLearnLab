from .models import Author, Book, Librarian, Library

for p in Book.objects.raw("SELECT * FROM Book WHERE Author= ''"):
    print(p)

for p in Library.objects.raw("SELECT books FROM Library "):
    print(p)    

for p in Librarian.objects.raw("DELETE name FROM Librarion WHERE Library=''"):
    print(p)       