# Generated by Django 3.2.20 on 2023-08-22 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20230822_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='membersrecord',
            name='date_of_issue',
            field=models.DateField(default=''),
        ),
        migrations.AddField(
            model_name='membersrecord',
            name='date_of_return',
            field=models.DateField(default=''),
        ),
    ]
