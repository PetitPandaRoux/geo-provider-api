# Generated by Django 3.2.6 on 2021-08-31 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0003_provideravailibility_provider_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provideravailibility',
            name='gps_x_coord',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='provideravailibility',
            name='gps_y_coord',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True),
        ),
    ]
