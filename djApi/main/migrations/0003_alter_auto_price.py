# Generated by Django 3.2.8 on 2021-11-10 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_auto_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='Цена авто'),
        ),
    ]
