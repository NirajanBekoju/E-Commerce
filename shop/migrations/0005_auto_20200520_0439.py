# Generated by Django 3.0.6 on 2020-05-20 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items_json',
            field=models.CharField(max_length=6000),
        ),
    ]
