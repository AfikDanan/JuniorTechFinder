# Generated by Django 4.1.7 on 2023-04-20 08:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Juniors', '0009_alter_juniors_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juniors',
            name='cv_file',
            field=models.FileField(blank=True, null=True, upload_to='media', validators=[django.core.validators.FileExtensionValidator(['pdf'], 'Only pdf files are allowed.')]),
        ),
    ]
