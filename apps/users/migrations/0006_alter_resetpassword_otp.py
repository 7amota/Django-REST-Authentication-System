# Generated by Django 5.1 on 2024-08-27 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_resetpassword_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassword',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]