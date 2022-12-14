# Generated by Django 4.1.3 on 2022-11-27 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Name')),
                ('description', models.TextField(max_length=1000, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Price')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
            },
        ),
    ]
