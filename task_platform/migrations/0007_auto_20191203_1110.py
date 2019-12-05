# Generated by Django 2.0.6 on 2019-12-03 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_platform', '0006_task_receive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='receiver',
        ),
        migrations.AddField(
            model_name='task',
            name='begin_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]