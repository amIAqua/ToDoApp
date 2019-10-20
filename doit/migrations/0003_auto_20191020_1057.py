# Generated by Django 2.2.5 on 2019-10-20 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doit', '0002_aboutpageinformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpageinformation',
            name='section2_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='aboutpageinformation',
            name='section3_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='aboutpageinformation',
            name='section4_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='aboutpageinformation',
            name='section_description1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='aboutpageinformation',
            name='title_description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='aboutpageinformation',
            name='title_section2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='aboutpageinformation',
            name='title_section3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='aboutpageinformation',
            name='title_section4',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]