# Generated by Django 4.0.3 on 2022-03-21 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_customer_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Primeiro Nome'),
        ),
    ]