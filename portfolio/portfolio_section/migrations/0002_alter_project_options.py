# Generated by Django 5.0.1 on 2024-01-20 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_section', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created_at']},
        ),
    ]