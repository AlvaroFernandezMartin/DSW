# Generated by Django 5.1.2 on 2024-10-08 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_alter_note_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=models.SlugField(max_length=140, unique=True),
        ),
    ]
