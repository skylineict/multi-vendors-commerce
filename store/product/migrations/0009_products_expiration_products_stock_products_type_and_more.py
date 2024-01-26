# Generated by Django 5.0.1 on 2024-01-25 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_products_vendors'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='expiration',
            field=models.CharField(blank=True, default='200 days', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='stock',
            field=models.CharField(blank=True, default='10', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='type',
            field=models.CharField(blank=True, default='best selling', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product_names',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='product.products'),
        ),
        migrations.AlterField(
            model_name='products',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
