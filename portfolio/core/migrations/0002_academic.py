# Generated by Django 5.0.1 on 2024-01-28 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('finished', models.BooleanField()),
                ('finish_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
    ]