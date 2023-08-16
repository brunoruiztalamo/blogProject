# Generated by Django 4.2.3 on 2023-08-16 18:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(db_column='Nombre', max_length=50)),
                ('descripcion_categoria', models.CharField(db_column='Descripcion', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='No Title', max_length=100)),
                ('header', models.CharField(default='No subtitle', max_length=100)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2023, 8, 16, 18, 34, 21, 274133, tzinfo=datetime.timezone.utc))),
                ('content', models.TextField(blank=True, default='No Content', max_length=10000)),
                ('image', models.ImageField(upload_to='posts/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2023, 8, 16, 18, 34, 21, 275488, tzinfo=datetime.timezone.utc))),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogPosts.post')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
