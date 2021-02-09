# Generated by Django 3.1.6 on 2021-02-09 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Кличка')),
                ('type', models.CharField(max_length=100, verbose_name='Вид питомца')),
                ('image', models.ImageField(upload_to='pets/', verbose_name='Фото питомца')),
            ],
            options={
                'verbose_name': 'Питомец',
                'verbose_name_plural': 'Питомцы',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.PositiveSmallIntegerField(default=100, verbose_name='Цена')),
                ('image', models.ImageField(upload_to='services/', verbose_name='Изображение')),
                ('url', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('tel_number', models.PositiveSmallIntegerField(default=0, help_text='начинать с семерки', verbose_name='Номер телефона')),
                ('animals', models.ManyToManyField(related_name='animal', to='pet_shop.Animal', verbose_name='питомец')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.AddField(
            model_name='animal',
            name='services',
            field=models.ManyToManyField(related_name='service', to='pet_shop.Service', verbose_name='услуга'),
        ),
    ]