# Generated by Django 4.2.6 on 2023-10-23 20:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audiofile',
            name='file_path',
        ),
        migrations.AddField(
            model_name='audiofile',
            name='audio',
            field=models.FileField(default=django.utils.timezone.now, upload_to='audio/'),
            preserve_default=False,
        ),
    ]
