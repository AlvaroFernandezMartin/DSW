# Generated by Django 5.1.2 on 2024-10-08 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_note_content_alter_note_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=models.SlugField(blank=True, max_length=140, unique=True),
        ),
    ]
