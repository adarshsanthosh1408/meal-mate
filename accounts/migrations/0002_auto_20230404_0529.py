# Generated by Django 2.2.9 on 2023-04-04 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='virtual_wallet_balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]