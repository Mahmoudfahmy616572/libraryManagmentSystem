# Generated by Django 4.2.4 on 2023-08-20 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='status',
        ),
    ]
