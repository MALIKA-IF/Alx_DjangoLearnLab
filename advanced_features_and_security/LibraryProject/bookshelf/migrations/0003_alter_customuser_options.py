# Generated by Django 5.1.6 on 2025-03-05 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0002_customuser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': [('can_view', 'can view'), ('can_create', 'can create'), ('can_edit', 'can edit'), ('can_delete', 'can delete')]},
        ),
    ]
