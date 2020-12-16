# Generated by Django 2.2 on 2019-04-12 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20190413_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.BookAuthor'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.BookCategory'),
        ),
    ]
