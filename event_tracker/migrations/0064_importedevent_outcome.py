# Generated by Django 4.1.7 on 2023-04-26 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_tracker', '0063_alter_credential_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='importedevent',
            name='outcome',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]