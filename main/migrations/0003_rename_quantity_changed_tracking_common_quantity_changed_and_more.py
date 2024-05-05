# Generated by Django 5.0.3 on 2024-04-08 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tracking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracking',
            old_name='quantity_changed',
            new_name='common_quantity_changed',
        ),
        migrations.AddField(
            model_name='tracking',
            name='once_quantity_changed',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
