from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission,User,Group
from .models import Admin,Viewer,Editor
from django.http import HttpResponse

# Create your views here.

#AUTH_USER_MODEL = "relationship_app.CustomUser()"
permission_required('bookshelf.can_edit', raise_exception=True)
def add_book(request):
    return HttpResponse("book added")
permission_required('bookshelf.can_view', raise_exception=True)
def add_book(request):
    return HttpResponse("book viewed")
permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    return HttpResponse("book created")
permission_required('bookshelf.can_delete', raise_exception=True)
def add_book(request):
    return HttpResponse("book deleted")



