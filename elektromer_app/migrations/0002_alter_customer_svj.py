# Generated by Django 4.2.6 on 2023-10-23 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elektromer_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='svj',
            field=models.ManyToManyField(to='elektromer_app.svj'),
        ),
    ]
