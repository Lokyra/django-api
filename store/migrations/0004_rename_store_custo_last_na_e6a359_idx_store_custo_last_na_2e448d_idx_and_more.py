# Generated by Django 5.1.1 on 2024-09-18 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_birth_rate_customer_birth_date_and_more'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='customer',
            new_name='store_custo_last_na_2e448d_idx',
            old_name='store_custo_last_na_e6a359_idx',
        ),
        migrations.AlterModelTable(
            name='customer',
            table='store_customer',
        ),
    ]
