# Generated by Django 4.0.4 on 2022-04-30 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_address_zip'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['last_name', 'first_name'], name='store_custo_last_na_2e448d_idx'),
        ),
        migrations.AlterModelTable(
            name='customer',
            table='store_customer',
        ),
    ]
