# Generated by Django 4.2.3 on 2023-07-24 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myService', '0021_alter_testimonials_image_alter_testimonials_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='status',
            field=models.BooleanField(default=False, help_text='***Check the Button to make it display on Your Site'),
        ),
    ]
