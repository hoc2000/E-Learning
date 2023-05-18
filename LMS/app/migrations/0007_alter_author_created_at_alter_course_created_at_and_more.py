# Generated by Django 4.1.8 on 2023-05-16 05:25

import app.models
import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_author_created_at_alter_course_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 16, 12, 25, 6, 697447), editable=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='course',
            name='update_at',
            field=app.models.AutoDateTimeField(default=django.utils.timezone.now),
        ),
    ]