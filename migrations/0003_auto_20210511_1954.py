# Generated by Django 3.2 on 2021-05-12 03:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_dietplan_hospitals'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietPlan1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('Age', models.IntegerField()),
                ('Goal', models.CharField(choices=[('Lose Weight', 'Lose Weight'), ('Maintain', 'Maintain'), ('Build Muscle', 'Build Muscle')], max_length=50)),
                ('Bodyfat', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=50)),
                ('Activity_level', models.CharField(choices=[('Lightly Active', 'Lightly Active'), ('Moderately Active', 'Moderately Active'), ('Highly Active', 'Highly Active'), ('Extremely Active', 'Extremely Active')], max_length=50)),
                ('Primary_Diet', models.CharField(choices=[('Anything', 'Anything'), ('Paleo', 'Paleo'), ('Vegetarian', 'Vegetarian'), ('Vegan', 'Vegan'), ('Ketogenic', 'Ketogenic'), ('Mediterranean', 'Mediterranean')], max_length=50)),
                ('Diet_photo', models.ImageField(upload_to='Diet-img')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hospitals1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('Phone', models.IntegerField()),
                ('City', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('Location', models.CharField(max_length=100)),
                ('Hospital_photo', models.ImageField(upload_to='Hospital-img')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='hospitals',
            name='user',
        ),
        migrations.DeleteModel(
            name='DietPlan',
        ),
        migrations.DeleteModel(
            name='Hospitals',
        ),
    ]
