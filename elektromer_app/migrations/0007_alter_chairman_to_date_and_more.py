# Generated by Django 4.2.6 on 2023-10-18 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elektromer_app', '0006_alter_chairman_to_date_alter_flat_to_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairman',
            name='to_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='historicalchairman',
            name='to_date',
            field=models.DateField(),
        ),
    ]
