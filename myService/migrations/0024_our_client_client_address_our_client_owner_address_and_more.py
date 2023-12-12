# Generated by Django 4.2.3 on 2023-07-24 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myService', '0023_our_client_client_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='our_client',
            name='client_address',
            field=models.CharField(blank=True, default='Client Address', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='our_client',
            name='owner_address',
            field=models.CharField(blank=True, default='Owner Address', help_text='Fill up these Entryes only if the client is an Organization', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='our_client',
            name='owner_alt_contact',
            field=models.CharField(blank=True, default=0, help_text='Fill up these Entryes only if the client is an Organization', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='our_client',
            name='owner_contact',
            field=models.CharField(blank=True, default=0, help_text='Fill up these Entryes only if the client is an Organization', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='our_client',
            name='owner_email',
            field=models.EmailField(blank=True, default='owner@email.com', help_text='Fill up these Entryes only if the client is an Organization', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='our_client',
            name='owner_name',
            field=models.CharField(blank=True, default='Owner Name', help_text='Fill up these Entryes only if the client is an Organization', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='our_client',
            name='client_alt_contact',
            field=models.CharField(blank=True, default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='our_client',
            name='client_contact',
            field=models.CharField(blank=True, default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='our_client',
            name='client_email',
            field=models.EmailField(blank=True, default='client@email.com', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='our_client',
            name='client_name',
            field=models.CharField(blank=True, default='Client Name', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='our_client',
            name='client_type',
            field=models.CharField(blank=True, choices=[('Organization', 'Organization'), ('Person', 'Person')], default=None, max_length=50, null=True),
        ),
    ]
