# Generated by Django 5.0 on 2023-12-10 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0003_rename_title_category_rename_title_category_titles'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]