# Generated by Django 3.1.3 on 2020-11-22 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_auto_20201122_0346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'verbose_name': 'device', 'verbose_name_plural': 'Devices'},
        ),
        migrations.AddField(
            model_name='device',
            name='link_downloaded',
            field=models.IntegerField(default=0, verbose_name='device downloaded link'),
        ),
        migrations.AddField(
            model_name='device',
            name='link_pending',
            field=models.IntegerField(default=0, verbose_name='device pending link'),
        ),
        migrations.AddField(
            model_name='device',
            name='link_received',
            field=models.IntegerField(default=0, verbose_name='device received link'),
        ),
    ]