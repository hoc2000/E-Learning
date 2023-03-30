# Generated by Django 4.1.3 on 2023-03-29 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_author_author_profile_alter_author_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 29, 16, 37, 33, 709929), editable=False),
        ),
        migrations.AlterField(
            model_name='categories',
            name='icon',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
