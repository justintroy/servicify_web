# Generated by Django 4.0.4 on 2022-06-09 05:17

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_servicetypes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicetypes',
            name='image',
            field=models.ImageField(blank=True, upload_to=dashboard.models.service_type_directory_path),
        ),
    ]
