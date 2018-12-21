# Generated by Django 2.0.2 on 2018-10-10 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DONE', '0007_project_baserate'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='apr',
            field=models.FloatField(blank=True, default=0.2674, null=True, verbose_name='Cost of money'),
        ),
        migrations.AddField(
            model_name='project',
            name='aprd',
            field=models.FloatField(blank=True, default=0.0008, null=True, verbose_name='APR per day'),
        ),
        migrations.AddField(
            model_name='project',
            name='aprh',
            field=models.FloatField(blank=True, default=9.3e-05, null=True, verbose_name='APR per hour'),
        ),
        migrations.AddField(
            model_name='project',
            name='hpd',
            field=models.PositiveSmallIntegerField(blank=True, default=8, null=True, verbose_name='Hours per day'),
        ),
    ]