# Generated by Django 4.2.6 on 2023-10-27 17:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0002_auto_20191216_0937"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="photo",
            name="file",
        ),
    ]
