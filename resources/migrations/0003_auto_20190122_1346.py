# Generated by Django 2.0.2 on 2019-01-22 18:46

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_resources_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='max_days',
            field=models.PositiveSmallIntegerField(blank=True, default=5, null=True, verbose_name='Maximum number of work days per week'),
        ),
        migrations.AlterField(
            model_name='resources',
            name='proficiency',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('project_mgmt', 'Project Management'), ('construction_mgmt', 'Construction Management'), ('architectural', 'Architectural'), ('mechanical', 'Mechanical'), ('electrical', 'Electrical'), ('construction', 'Construction'), ('engineering', 'Engineering'), ('aviation', 'Aviation'), ('r_d', 'R&D'), ('power_energy', 'Power / Energy'), ('manufacturing', 'Manufacturing'), ('process', 'Process'), ('environmental', 'Environmental'), ('maritime_marine', 'Maritime / Marine'), ('military', 'Military'), ('multi_eng_construction', 'Multidiscipline engineering / construction')], max_length=201, verbose_name='Proficiency'),
        ),
    ]