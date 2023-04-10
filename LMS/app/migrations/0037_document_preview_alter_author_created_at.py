# Generated by Django 4.1.3 on 2023-03-30 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_document_lessson_alter_author_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='preview',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 30, 16, 24, 23, 137864), editable=False),
        ),
    ]