# Generated by Django 4.1.8 on 2023-04-10 05:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0059_alter_author_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 10, 12, 54, 7, 851970), editable=False),
        ),
    ]
