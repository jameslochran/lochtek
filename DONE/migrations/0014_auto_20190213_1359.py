# Generated by Django 2.0.2 on 2019-02-13 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DONE', '0013_auto_20181212_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Project Title'),
        ),
    ]