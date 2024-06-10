# Generated by Django 3.2.8 on 2021-11-10 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event_tracker', '0016_auto_20211109_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]