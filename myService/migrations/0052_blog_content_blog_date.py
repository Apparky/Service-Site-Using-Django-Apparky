# Generated by Django 4.2.3 on 2023-11-05 15:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myService', '0051_alter_blog_content_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_content',
            name='Blog_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
