# Generated by Django 5.1 on 2024-12-10 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_advertiser_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertiser',
            name='category',
        ),
        migrations.RemoveField(
            model_name='advertiser',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='AdvertCategory',
        ),
        migrations.DeleteModel(
            name='Advertiser',
        ),
        migrations.DeleteModel(
            name='Merchant',
        ),
    ]