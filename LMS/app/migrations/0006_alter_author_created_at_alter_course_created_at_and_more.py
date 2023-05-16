# Generated by Django 4.1.8 on 2023-05-16 05:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_course_update_at_alter_author_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 16, 12, 22, 38, 447115), editable=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
