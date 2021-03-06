# Generated by Django 3.1.3 on 2020-11-22 00:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'verbose_name': 'دستگاه', 'verbose_name_plural': 'دستگاه ها'},
        ),
        migrations.AddField(
            model_name='device',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is device active'),
        ),
        migrations.AddField(
            model_name='device',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='update date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='device',
            name='title',
            field=models.CharField(max_length=255, verbose_name='device title'),
        ),
        migrations.AlterField(
            model_name='device',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='udevice', to='accounts.user', verbose_name='user'),
        ),
    ]
