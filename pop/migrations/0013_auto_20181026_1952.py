# Generated by Django 2.1.2 on 2018-10-26 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pop', '0012_case_founder_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='pet_breed',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='pet_type',
            field=models.CharField(max_length=30, null=True),
        ),
    ]