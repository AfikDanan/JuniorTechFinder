# Generated by Django 4.1.7 on 2023-04-15 17:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Juniors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z\\s]*$', 'Only alphabetical characters are allowed.')])),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)])),
                ('city', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z\\s]*$', 'Only alphabetical characters are allowed.')])),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(120)])),
                ('skills', models.TextField(validators=[django.core.validators.RegexValidator('^[a-zA-Z\\s,]*$', 'Only alphabetical characters and commas are allowed.')])),
                ('summary', models.TextField()),
                ('cv_file', models.FileField(upload_to='media')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media')),
            ],
        ),
    ]