# Generated by Django 4.2.9 on 2024-02-08 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=5),
        ),
    ]