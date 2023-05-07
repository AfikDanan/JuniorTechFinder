# Generated by Django 4.1.7 on 2023-05-07 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Recruiters', '0004_alter_joblisting_recruiter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='recruiter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]