# Generated by Django 4.1.2 on 2023-01-11 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="app",
            name="otp_code",
            field=models.TextField(default="null"),
        ),
    ]
