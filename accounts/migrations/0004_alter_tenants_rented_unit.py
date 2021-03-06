# Generated by Django 4.0.2 on 2022-02-27 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental_property', '0005_alter_rentalunit_maintanance_status'),
        ('accounts', '0003_remove_profile_prefered_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenants',
            name='rented_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tenants', to='rental_property.rentalunit'),
        ),
    ]
