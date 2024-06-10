# Generated by Django 3.2.8 on 2021-10-20 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_tracker', '0009_auto_20211020_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='mitre_attack_subtechnique',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='event_tracker.attacksubtechnique'),
        ),
        migrations.AlterField(
            model_name='event',
            name='mitre_attack_tactic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='event_tracker.attacktactic'),
        ),
        migrations.AlterField(
            model_name='event',
            name='mitre_attack_technique',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='event_tracker.attacktechnique'),
        ),
    ]