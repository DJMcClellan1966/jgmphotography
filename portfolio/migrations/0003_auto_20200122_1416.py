# Generated by Django 3.0.2 on 2020-01-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_portfolio_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='summary',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
