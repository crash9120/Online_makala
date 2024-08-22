# Generated by Django 5.0.7 on 2024-08-05 11:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='article_like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_like', models.DateTimeField(auto_now_add=True)),
                ('article_like', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.arcticle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Makala halanan',
                'verbose_name_plural': 'Makala halanlar',
                'db_table': 'article_likes',
            },
        ),
        migrations.CreateModel(
            name='article_read',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_read', models.DateTimeField(auto_now_add=True)),
                ('article_read', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.arcticle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Makala okan',
                'verbose_name_plural': 'Makala okanlar',
                'db_table': 'article_reads',
                'ordering': ['date_read'],
            },
        ),
    ]
