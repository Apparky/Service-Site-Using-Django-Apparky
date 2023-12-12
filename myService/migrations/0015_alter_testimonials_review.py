# Generated by Django 4.2.3 on 2023-07-23 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myService', '0014_testimonials_testimonials_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='review',
            field=models.CharField(choices=[('Worst', 'Worst'), ('Bad', 'Bad'), ('Normal', 'Normal'), ('Good', 'Good'), ('Excellent', 'Excellent'), (None, None)], default=None, max_length=50),
        ),
    ]