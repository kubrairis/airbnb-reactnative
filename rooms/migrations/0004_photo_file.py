# Generated by Django 4.2.6 on 2023-10-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0003_remove_photo_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="photo",
            name="file",
            field=models.ImageField(default="1.webp", upload_to=""),
        ),
    ]
