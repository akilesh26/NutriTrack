# Generated by Django 5.1.1 on 2024-09-29 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0008_alter_user_item_banner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_item",
            name="banner",
            field=models.ImageField(blank=True, default="fallback.png", upload_to=""),
        ),
    ]
