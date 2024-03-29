# Generated by Django 4.2.10 on 2024-02-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_alter_adminwallet_balance_alter_wallet_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminwallet',
            name='balance',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
