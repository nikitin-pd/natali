# Generated by Django 3.1.4 on 2021-04-26 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50, verbose_name='Название услуги')),
                ('service_description', models.TextField(verbose_name='Описание услуги')),
                ('session_id', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50, verbose_name='Название услуги')),
                ('service_photo', models.ImageField(upload_to='', verbose_name='Фотография услуги')),
                ('service_description', models.TextField(verbose_name='Описание услуги')),
                ('service_price', models.IntegerField(verbose_name='Цена услуги')),
                ('release_date', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
