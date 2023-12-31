# Generated by Django 3.2.20 on 2023-08-22 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_membersrecord_signuprecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='membersrecord',
            name='book_details',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.books'),
        ),
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
