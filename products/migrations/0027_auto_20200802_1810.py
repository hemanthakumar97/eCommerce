# Generated by Django 2.2 on 2020-08-02 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20200802_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectronicComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('item_weight', models.CharField(blank=True, max_length=50, null=True)),
                ('product_dim', models.CharField(blank=True, max_length=50, null=True)),
                ('part_no', models.CharField(blank=True, max_length=50, null=True)),
                ('battery', models.CharField(blank=True, max_length=50, null=True)),
                ('audi_focus', models.CharField(blank=True, max_length=50, null=True)),
                ('programmable_btn', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('hardware_interface', models.CharField(blank=True, max_length=50, null=True)),
                ('voltage', models.CharField(blank=True, max_length=50, null=True)),
                ('color_screen', models.CharField(blank=True, max_length=50, null=True)),
                ('screen_size', models.CharField(blank=True, max_length=50, null=True)),
                ('compabitable_devises', models.CharField(blank=True, max_length=50, null=True)),
                ('property_1', models.TextField(blank=True, null=True)),
                ('property_2', models.TextField(blank=True, null=True)),
                ('property_3', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='electronic_components',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ElectronicComponent'),
        ),
        migrations.DeleteModel(
            name='ElectronicComponents',
        ),
    ]