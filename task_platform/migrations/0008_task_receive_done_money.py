# Generated by Django 2.0.6 on 2019-12-05 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_platform', '0007_auto_20191203_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_receive',
            name='done_money',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]