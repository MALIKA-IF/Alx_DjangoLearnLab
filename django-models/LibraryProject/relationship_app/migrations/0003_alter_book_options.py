# Generated by Django 5.1.6 on 2025-03-05 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_edit_book', 'can edit a book'), ('can_change_book', 'can change a book'), ('can_delete_book', 'can delete a book'), ('can_create_book', 'can create a book')]},
        ),
    ]
