# Generated by Django 4.2.10 on 2024-02-28 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recipe",
            old_name="image_alt",
            new_name="image_description",
        ),
    ]
