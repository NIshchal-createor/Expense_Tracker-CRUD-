# Generated by Django 5.0.6 on 2024-06-25 15:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(validators=[django.core.validators.MaxLengthValidator(255), django.core.validators.MinLengthValidator(10)])),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_At', models.DateTimeField(auto_now_add=True)),
                ('updated_At', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
