# Generated by Django 3.0.8 on 2020-08-27 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0002_auto_20200827_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailentry',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='emailentry',
            name='name',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
