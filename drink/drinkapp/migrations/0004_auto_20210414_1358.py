# Generated by Django 3.1.7 on 2021-04-14 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinkapp', '0003_auto_20210414_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='location',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='abc',
            field=models.TextField(default='default'),
        ),
    ]
