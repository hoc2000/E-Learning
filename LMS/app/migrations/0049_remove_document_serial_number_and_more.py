# Generated by Django 4.1.3 on 2023-04-05 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_alter_author_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='serial_number',
        ),
        migrations.AlterField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 5, 22, 54, 22, 761219), editable=False),
        ),
    ]
