# Generated by Django 2.2 on 2020-08-13 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='products',
            new_name='product',
        ),
    ]
