# Generated by Django 3.2 on 2021-05-18 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitnesscenter',
            name='Location',
            field=models.CharField(max_length=900),
        ),
    ]