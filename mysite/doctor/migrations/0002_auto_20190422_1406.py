# Generated by Django 2.2 on 2019-04-22 14:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]