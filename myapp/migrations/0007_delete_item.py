# Generated by Django 5.1.1 on 2024-09-28 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0006_rename_cloth_brand_user_item_brand_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Item",
        ),
    ]
