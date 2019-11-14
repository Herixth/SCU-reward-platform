# Generated by Django 2.2.7 on 2019-11-14 06:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task_platform', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['pub_time'], 'verbose_name': '任务', 'verbose_name_plural': '任务'},
        ),
        migrations.AddField(
            model_name='task',
            name='task_description',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
