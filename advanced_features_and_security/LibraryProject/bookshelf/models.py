from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission



# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    publication_year=models.IntegerField()

class CustomUser(AbstractUser):
    date_of_birth=models.DateField()
    profile_photo=models.ImageField()    
#can_view, can_create, can_edit, and can_delete
    class Meta:
        permissions =[
            ("can_view","can view"),
            ("can_create","can create"),
            ("can_edit","can edit"),
             ("can_delete","can delete"),

        ]


class CustomUserManager(BaseUserManager):
    def create_user(self, email="None", password="None"):
        pass
    def create_superuser(self,email="None", password="None"):
        pass


admin_group =Group.objects.create(name='Admins')
editor_group = Group.objects.create(name='Editors')
viewer_group=Group.objects.create(name='Viewers')

   
view_permission = Permission.objects.get(codename='can_view')
create_permission = Permission.objects.get(codename='can_create')
edit_permission = Permission.objects.get(codename='can_edit')
delete_permission = Permission.objects.get(codename='can_delete')

admin_group.permissions.add(view_permission)
admin_group.permissions.add(create_permission)
admin_group.permissions.add(edit_permission)
admin_group.permissions.add(delete_permission)

editor_group.permissions.add(editor_group)
editor_group.permissions.add(create_permission)

viewer_group.permissions.add(view_permission)




