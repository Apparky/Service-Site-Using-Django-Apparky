# Generated by Django 4.2.3 on 2023-07-25 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myService', '0031_rename_client_status_our_client_priority_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Portfolio_name', models.CharField(blank=True, default='Portfolio Name', max_length=100, null=True)),
                ('Portfolio_type', models.CharField(blank=True, choices=[('Web Development', 'Web Development'), ('Desktop Applications', 'Desktop Applications'), ('Mobile Applications', 'Mobile Applications'), ('Next JS SEO', 'Next JS SEO'), (None, None)], default=None, max_length=100, null=True)),
                ('Portfolio_summary', models.CharField(blank=True, default='Portfolio Summary', max_length=300, null=True)),
                ('Portfolio_Description', models.TextField(blank=True, default='Portfolio Description', null=True)),
                ('portfolio_slug', models.SlugField(blank=True, default='portfolio_slug', max_length=100, null=True)),
                ('portfolio_image', models.ImageField(blank=True, help_text='**You can only add one Picture', null=True, upload_to='media/images/')),
                ('Portfolio_Display_Status', models.BooleanField(default=False)),
            ],
        ),
    ]