# Generated by Django 4.1.7 on 2023-05-19 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Juniors', '0012_alter_juniors_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='juniors',
            name='generated_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
