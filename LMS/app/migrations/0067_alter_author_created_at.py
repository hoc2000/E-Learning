# Generated by Django 4.1.8 on 2023-04-25 07:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0066_alter_author_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 25, 14, 37, 42, 978006), editable=False),
        ),
    ]
