# Generated by Django 4.2.3 on 2023-07-22 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myService', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='our_team',
            name='alt_contact_no',
            field=models.CharField(blank=True, default=0, max_length=20, null=True),
        ),
    ]
