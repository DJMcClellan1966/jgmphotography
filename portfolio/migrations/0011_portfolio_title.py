# Generated by Django 3.0.2 on 2020-02-01 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_portfolio_photographer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
