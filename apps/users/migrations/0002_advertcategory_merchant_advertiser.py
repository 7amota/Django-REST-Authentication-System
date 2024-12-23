# Generated by Django 5.1 on 2024-08-27 07:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_activated', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('city', models.CharField(max_length=350)),
                ('area', models.CharField(max_length=350)),
                ('description', models.TextField(blank=True, null=True)),
                ('facebook', models.CharField(blank=True, max_length=550, null=True)),
                ('instagram', models.CharField(blank=True, max_length=550, null=True)),
                ('twitter', models.CharField(blank=True, max_length=550, null=True)),
                ('is_activated', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(to='users.advertcategory')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.user',),
        ),
    ]
