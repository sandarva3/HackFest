# Generated by Django 5.0.1 on 2024-01-12 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samasya', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]