# Generated by Django 5.0 on 2023-12-19 18:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_category_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="Category",
        ),
    ]
