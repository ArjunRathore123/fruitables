# Generated by Django 4.2.9 on 2024-02-09 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_alter_order_order_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_notes',
        ),
    ]
