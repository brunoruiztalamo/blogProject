# Generated by Django 4.2.3 on 2023-08-16 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogProfiles', '0002_remove_userprofile_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
