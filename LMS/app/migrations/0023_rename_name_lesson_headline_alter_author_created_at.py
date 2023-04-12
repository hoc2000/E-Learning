# Generated by Django 4.1.3 on 2023-03-29 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_author_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='name',
            new_name='headline',
        ),
        migrations.AlterField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 29, 14, 53, 44, 878529)),
        ),
    ]
