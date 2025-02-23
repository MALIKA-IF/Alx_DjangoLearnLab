from .models import Author, Book, Librarian, Library

Library.objects.get(name='Library_name')

   

for p in Library.objects.raw("SELECT books FROM Library "):
    print(p)    

for p in Librarian.objects.raw("DELETE name FROM Librarion WHERE Library=''"):
    print(p)       