# Generated by Django 2.1.4 on 2019-01-07 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AWSAccount',
            new_name='aws_account',
        ),
    ]
