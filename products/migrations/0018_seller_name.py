# Generated by Django 2.2 on 2020-08-02 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_remove_seller_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
