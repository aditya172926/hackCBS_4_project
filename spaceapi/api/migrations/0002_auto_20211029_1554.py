# Generated by Django 3.2.7 on 2021-10-29 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='continent',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='userdata',
            name='country',
            field=models.CharField(default='', max_length=50),
        ),
    ]
