# Generated by Django 4.0.10 on 2023-06-06 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_course_department_alter_department_image_dep'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='department',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
