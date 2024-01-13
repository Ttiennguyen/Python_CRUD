# Generated by Django 5.0.1 on 2024-01-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_member_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.CharField(max_length=50, null=True),
        ),
    ]