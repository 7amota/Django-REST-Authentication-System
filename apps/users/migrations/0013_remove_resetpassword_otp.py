# Generated by Django 5.1 on 2024-12-11 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_user_phonenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resetpassword',
            name='otp',
        ),
    ]
