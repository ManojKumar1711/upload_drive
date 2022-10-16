# Generated by Django 4.1.2 on 2022-10-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("owner_name", models.CharField(max_length=50)),
                ("file", models.FileField(upload_to="upload/files/")),
            ],
        ),
    ]
