# Generated by Django 4.2 on 2023-04-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electric_vehicles', '0003_alter_electricvehicle_cafv_eligibility_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electricvehicle',
            name='census_tract',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
