# Generated by Django 5.0.4 on 2024-05-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]