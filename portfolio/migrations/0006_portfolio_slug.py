# Generated by Django 3.0.2 on 2020-01-23 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_remove_portfolio_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
