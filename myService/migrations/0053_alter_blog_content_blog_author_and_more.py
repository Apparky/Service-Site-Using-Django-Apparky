# Generated by Django 4.2.3 on 2023-11-05 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myService', '0052_blog_content_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_content',
            name='Blog_Author',
            field=models.ForeignKey(help_text='***** Add Auther User Name *****', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog_content',
            name='Blog_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]