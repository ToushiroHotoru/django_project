# Generated by Django 3.1.6 on 2021-02-09 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet_shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='full_name',
            new_name='name',
        ),
    ]
