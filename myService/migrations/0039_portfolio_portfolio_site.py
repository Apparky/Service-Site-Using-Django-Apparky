# Generated by Django 4.2.3 on 2023-07-27 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myService', '0038_alter_portfolio_portfolio_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='portfolio_site',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
