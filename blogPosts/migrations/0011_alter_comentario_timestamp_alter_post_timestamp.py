# Generated by Django 4.2.3 on 2023-08-17 06:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPosts', '0010_alter_comentario_timestamp_alter_post_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 6, 5, 35, 871238, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 6, 5, 35, 871238, tzinfo=datetime.timezone.utc)),
        ),
    ]
