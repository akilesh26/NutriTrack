# Generated by Django 5.1.1 on 2024-09-29 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0007_delete_item"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_item",
            name="banner",
            field=models.ImageField(
                blank=True, default="fallback.png", upload_to="media/"
            ),
        ),
    ]
