# Generated by Django 3.2.20 on 2023-08-22 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20230822_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membersrecord',
            name='date_of_issue',
        ),
        migrations.RemoveField(
            model_name='membersrecord',
            name='date_of_return',
        ),
    ]
