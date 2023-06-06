# Generated by Django 4.1.8 on 2023-05-23 07:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_author_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(
                default=django.utils.timezone.now, editable=False),
        ),
    ]
