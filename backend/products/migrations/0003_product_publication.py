# Generated by Django 4.2.3 on 2023-07-11 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='publication',
            field=models.BooleanField(default=True),
        ),
    ]
