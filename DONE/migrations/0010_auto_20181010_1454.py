# Generated by Django 2.0.2 on 2018-10-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DONE', '0009_auto_20181010_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='baserate',
            field=models.PositiveSmallIntegerField(blank=True, default=90, null=True),
        ),
    ]
