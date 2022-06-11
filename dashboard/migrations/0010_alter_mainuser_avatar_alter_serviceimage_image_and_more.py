# Generated by Django 4.0.4 on 2022-05-24 11:08

import dashboard.custom_models.compressed_image_field
import dashboard.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_servicereview_alter_mainuser_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainuser',
            name='avatar',
            field=dashboard.custom_models.compressed_image_field.CompressedImageField(default='users/avatar.png', quality=50, upload_to=dashboard.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='serviceimage',
            name='image',
            field=dashboard.custom_models.compressed_image_field.CompressedImageField(quality=50, upload_to=dashboard.models.service_directory_path),
        ),
        migrations.AlterField(
            model_name='servicereviewimage',
            name='image',
            field=dashboard.custom_models.compressed_image_field.CompressedImageField(quality=25, upload_to=dashboard.models.service_review_directory_path),
        ),
        migrations.AlterField(
            model_name='workofferimage',
            name='image',
            field=dashboard.custom_models.compressed_image_field.CompressedImageField(quality=50, upload_to=dashboard.models.workoffer_directory_path),
        ),
    ]
