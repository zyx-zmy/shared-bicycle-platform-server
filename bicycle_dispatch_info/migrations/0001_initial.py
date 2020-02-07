# Generated by Django 2.2.8 on 2020-02-07 06:47

from django.db import migrations, models
import utils.uu32_helper


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BicycleDispatchInfo',
            fields=[
                ('bicycle_dispatch_info_id', models.CharField(default=utils.uu32_helper.uuid32, max_length=32, primary_key=True, serialize=False)),
                ('remote_record_id', models.CharField(max_length=100)),
                ('company_id', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('bicycle_number', models.CharField(max_length=100)),
                ('dispatch_status', models.IntegerField()),
                ('dispatcher', models.CharField(max_length=100)),
                ('dispatcher_phone', models.CharField(max_length=100)),
                ('dispatch_start_lon', models.CharField(max_length=100)),
                ('dispatch_start_lat', models.CharField(max_length=100)),
                ('dispatch_end_lon', models.CharField(max_length=100)),
                ('dispatch_end_lat', models.CharField(max_length=100)),
                ('dispatch_start_time', models.CharField(max_length=100)),
                ('dispatch_end_time', models.CharField(max_length=100)),
                ('dispatch_start_addr', models.CharField(max_length=100)),
                ('dispatch_end_addr', models.CharField(max_length=100)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bicycle_dispatch_info',
            },
        ),
    ]
