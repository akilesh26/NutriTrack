# Generated by Django 5.1.1 on 2024-09-28 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_alter_user_item_cloth_size"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user_item",
            old_name="cloth_brand",
            new_name="brand",
        ),
        migrations.RenameField(
            model_name="user_item",
            old_name="cloth_color",
            new_name="color",
        ),
        migrations.RenameField(
            model_name="user_item",
            old_name="cloth_size",
            new_name="size",
        ),
        migrations.RenameField(
            model_name="user_item",
            old_name="cloth_type",
            new_name="type",
        ),
    ]
