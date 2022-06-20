# Generated by Django 4.0.5 on 2022-06-20 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('Discription', models.TextField()),
                ('item_cost', models.IntegerField()),
                ('stock_quantity', models.IntegerField()),
                ('volume', models.PositiveIntegerField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ProductDetails',
        ),
    ]
