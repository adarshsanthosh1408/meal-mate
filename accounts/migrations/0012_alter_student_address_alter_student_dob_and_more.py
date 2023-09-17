# Generated by Django 4.2 on 2023-04-07 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_student_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1),
        ),
    ]