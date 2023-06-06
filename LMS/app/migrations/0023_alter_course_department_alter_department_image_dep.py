# Generated by Django 4.1.8 on 2023-05-25 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_department_image_dep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='author',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.author'),
        ),
        migrations.AlterField(
            model_name='author',
            name='image_dep',
            field=models.ImageField(null=True, upload_to='featured_img'),
        ),
    ]
