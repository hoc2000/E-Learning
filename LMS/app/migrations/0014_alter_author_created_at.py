# Generated by Django 4.1.8 on 2023-05-21 16:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_author_created_at_alter_course_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 21, 23, 4, 40, 342185), editable=False),
        ),
    ]