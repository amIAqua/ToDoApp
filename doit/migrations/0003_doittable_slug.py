# Generated by Django 2.2.5 on 2019-10-24 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doit', '0002_auto_20191023_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='doittable',
            name='slug',
            field=models.SlugField(default=' '),
        ),
    ]