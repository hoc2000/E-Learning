# Generated by Django 4.1.8 on 2023-05-23 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_course_department_alter_course_date_start_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(null=True, upload_to='featured_img'),
        ),
    ]
