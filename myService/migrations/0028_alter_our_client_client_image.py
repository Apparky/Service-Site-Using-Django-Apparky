# Generated by Django 4.2.3 on 2023-07-24 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myService', '0027_our_client_client_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='our_client',
            name='client_image',
            field=models.ImageField(blank=True, default='**You can only add one Image', null=True, upload_to='media/images/'),
        ),
    ]