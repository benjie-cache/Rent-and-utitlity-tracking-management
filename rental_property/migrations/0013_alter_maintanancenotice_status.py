# Generated by Django 4.0.2 on 2022-03-22 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_property', '0012_maintanancenotice_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintanancenotice',
            name='status',
            field=models.CharField(default='In Progress', max_length=20),
        ),
    ]
