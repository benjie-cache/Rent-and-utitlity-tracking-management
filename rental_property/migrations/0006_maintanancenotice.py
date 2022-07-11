# Generated by Django 4.0.2 on 2022-03-07 18:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_tenants_rented_unit'),
        ('rental_property', '0005_alter_rentalunit_maintanance_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintananceNotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_number', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('from_date_time', models.DateTimeField()),
                ('to_date_time', models.DateTimeField()),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rental_property.building')),
                ('notice_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.managers')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rental_property.rentalunit')),
            ],
        ),
    ]