# Generated by Django 4.2.9 on 2024-02-09 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_remove_order_order_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]