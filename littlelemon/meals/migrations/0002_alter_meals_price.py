# Generated by Django 5.1.1 on 2024-10-06 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]