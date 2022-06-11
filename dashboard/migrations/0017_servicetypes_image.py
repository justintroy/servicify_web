# Generated by Django 4.0.4 on 2022-06-09 05:04

import dashboard.custom_models.compressed_image_field
import dashboard.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_service_city_service_full_addr_service_locality_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetypes',
            name='image',
            field=dashboard.custom_models.compressed_image_field.CompressedImageField(blank=True, quality=25, upload_to=dashboard.models.service_type_directory_path),
        ),
    ]
