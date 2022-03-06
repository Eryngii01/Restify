# Generated by Django 4.0.2 on 2022-03-06 01:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurants', '0002_post_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='followers',
            field=models.ManyToManyField(default=0, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
