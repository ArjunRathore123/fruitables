# Generated by Django 4.2.9 on 2024-02-09 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_cartitem_quantity_alter_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
    ]
