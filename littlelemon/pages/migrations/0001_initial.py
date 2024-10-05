# Generated by Django 5.1.1 on 2024-10-05 09:56

import django.db.models.deletion
import django.utils.timezone
import pages.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('bill_id', models.UUIDField(default=pages.models.generate_unique_id, editable=False, primary_key=True, serialize=False)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_paid', models.BooleanField(default=False)),
                ('payment_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('meal_id', models.UUIDField(default=pages.models.generate_unique_id, editable=False, primary_key=True, serialize=False)),
                ('name_meal', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=pages.models.generate_unique_id, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('is_loggedin', models.BooleanField(default=False)),
                ('role', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.UUIDField(default=pages.models.generate_unique_id, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.bill')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.meal')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='bill_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.user'),
        ),
    ]
