# Generated by Django 3.2.8 on 2021-10-19 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='code',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]