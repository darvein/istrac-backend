# Generated by Django 5.0 on 2024-01-19 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_event_created_by_alter_photo_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='slug',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
