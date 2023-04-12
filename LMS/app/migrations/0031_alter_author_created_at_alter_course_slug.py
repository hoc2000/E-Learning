# Generated by Django 4.1.3 on 2023-03-29 09:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_alter_author_created_at_alter_categories_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 29, 16, 47, 8, 730846), editable=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False, max_length=500, null=True),
        ),
    ]
