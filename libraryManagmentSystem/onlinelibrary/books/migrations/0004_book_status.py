# Generated by Django 4.2.4 on 2023-08-20 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_auther_book_borrowed_book_borrowed_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('Available', 'a'), ('Borrowed', 'b')], default='Available', max_length=10),
        ),
    ]
