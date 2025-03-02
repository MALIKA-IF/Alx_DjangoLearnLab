from django.contrib import admin
from .models import Book,CustomUser,CustomUserManager


# Register your models here.

admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year')
    search_fields = ('title', 'author')

#admin.site.register(Book, BookAdmin)
class CustomUserAdmin(admin.ModelAdmin):
    list_display_CustomUser = ('date_of_birth', 'profile_photo')
    
admin.site.register(CustomUser, CustomUserAdmin)