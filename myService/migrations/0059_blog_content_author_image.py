# Generated by Django 4.2.3 on 2023-11-07 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myService', '0058_blog_content_headline_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_content',
            name='Author_Image',
            field=models.ImageField(blank=True, help_text='***** Update Auther Image Over Here *****', null=True, upload_to='media/images/'),
        ),
    ]
