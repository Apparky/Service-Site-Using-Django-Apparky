# Generated by Django 4.2.3 on 2024-01-06 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myService', '0002_rename_contact_header_and_info_dumy_contact_header_and_info'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Testimonials',
            new_name='Testimonial',
        ),
    ]
