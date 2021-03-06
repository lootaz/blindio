# Generated by Django 2.0.1 on 2018-02-07 08:07

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FSItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_ts', models.DateTimeField(auto_now_add=True)),
                ('update_ts', models.DateTimeField(auto_now=True)),
                ('delete_ts', models.DateTimeField(null=True)),
                ('path', models.CharField(max_length=1024)),
            ],
            options={
                'db_table': 'blindio_fsitem',
            },
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_ts', models.DateTimeField(null=True)),
                ('finish_ts', models.DateTimeField(null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('fs_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                              to='blindio_monitor.FSItem')),
            ],
            options={
                'db_table': 'blindio_study',
            },
        ),
    ]
