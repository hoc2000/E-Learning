# Generated by Django 4.1.3 on 2023-04-04 07:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_rename_lessson_video_lesson_alter_author_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='preview',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 4, 14, 56, 50, 301962), editable=False),
        ),
    ]
