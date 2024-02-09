# Generated by Django 4.2.9 on 2024-02-09 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_wallet_adminwallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminwallet',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
