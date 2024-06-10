# Generated by Django 3.2.8 on 2021-10-19 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('host', models.CharField(max_length=100)),
                ('process', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('operator', models.CharField(max_length=5)),
                ('mitre_ref', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='source', to='event_tracker.context')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='target', to='event_tracker.context')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_tracker.task')),
            ],
        ),
    ]