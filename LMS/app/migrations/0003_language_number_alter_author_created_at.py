# Generated by Django 4.1.8 on 2023-05-16 04:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_author_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(
                2023, 5, 16, 11, 57, 51, 893040), editable=False),
        ),
    ]
