# Generated by Django 4.2.5 on 2023-09-13 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='type_project',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
