# Generated by Django 5.1.1 on 2024-09-28 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_user_item_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_item",
            name="cloth_size",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Extra Small", "XS"),
                    ("small", "S"),
                    ("medium", "M"),
                    ("Large", "L"),
                    ("Extra Large", "XL"),
                ],
                max_length=100,
            ),
        ),
    ]
