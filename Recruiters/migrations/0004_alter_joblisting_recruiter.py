# Generated by Django 4.1.7 on 2023-05-07 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recruiters', '0003_alter_joblisting_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='recruiter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recruiters.recruiters'),
        ),
    ]