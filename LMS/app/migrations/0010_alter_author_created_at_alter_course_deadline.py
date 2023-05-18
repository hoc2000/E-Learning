# Generated by Django 4.1.8 on 2023-05-18 03:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_author_created_at_alter_document_file_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 18, 10, 27, 1, 459374), editable=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
    ]
