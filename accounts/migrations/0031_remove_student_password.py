# Generated by Django 4.1.6 on 2023-07-18 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
    ]
