# Generated by Django 5.0.1 on 2024-01-13 00:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samasya', '0006_customer_city_customer_district_customer_province_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='samasya.post'),
        ),
    ]
