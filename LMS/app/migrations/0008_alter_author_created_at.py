# Generated by Django 4.1.8 on 2023-05-16 05:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_author_created_at_alter_course_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(
                2023, 5, 16, 12, 37, 44, 344625), editable=False),
        ),
    ]
