# Generated by Django 4.0.1 on 2022-02-15 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_name_category_title_rename_title_food_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
    ]