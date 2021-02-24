# Generated by Django 3.1.7 on 2021-02-24 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker_app', '0002_remove_ticket_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('New', 'NEW'), ('In Progress', 'INPROGRESS'), ('Done', 'DONE'), ('Invalid', 'INVALID')], default='New', max_length=20),
        ),
    ]
