# Generated by Django 3.1.7 on 2021-02-24 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='created_by',
        ),
    ]
