# Generated by Django 4.2 on 2023-04-10 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_menuitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='image',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='images',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]