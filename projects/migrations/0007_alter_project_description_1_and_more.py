# Generated by Django 4.2.5 on 2023-09-13 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_rename_description_project_description_5_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_5',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_6',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='project',
            name='display',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='modeling',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='planimetry',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='posproduction',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='software',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='type_project',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='vegetation',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
