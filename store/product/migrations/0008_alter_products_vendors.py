# Generated by Django 5.0.1 on 2024-01-24 02:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_products_category'),
        ('vendor', '0002_vendor_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='vendors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='vendor.vendor'),
        ),
    ]
