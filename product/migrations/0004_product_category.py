# Generated by Django 5.0 on 2023-12-19 22:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_remove_category_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
