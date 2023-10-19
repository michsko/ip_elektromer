# Generated by Django 4.2.6 on 2023-10-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elektromer_app', '0007_alter_chairman_to_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chairman',
            name='to_date',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='to_date',
        ),
        migrations.RemoveField(
            model_name='gsm_modul',
            name='to_date',
        ),
        migrations.RemoveField(
            model_name='historicalchairman',
            name='to_date',
        ),
        migrations.RemoveField(
            model_name='historicalcustomer',
            name='svj',
        ),
        migrations.RemoveField(
            model_name='historicalflat',
            name='to_date',
        ),
        migrations.RemoveField(
            model_name='historicalgsm_modul',
            name='to_date',
        ),
        migrations.RemoveField(
            model_name='historicalmain_electrometer',
            name='to_date',
        ),
        migrations.RemoveField(
            model_name='historicalsolar_electrometer',
            name='to_date',
        ),
        migrations.RemoveField(
            model_name='historicalsub_chairman',
            name='to_date',
        ),
        migrations.RemoveField(
            model_name='historicalsvj',
            name='to_date',
        ),
        migrations.RemoveField(
            model_name='main_electrometer',
            name='to_date',
        ),
        migrations.RemoveField(
            model_name='solar_electrometer',
            name='to_date',
        ),
        migrations.RemoveField(
            model_name='sub_chairman',
            name='to_date',
        ),
        migrations.RemoveField(
            model_name='sub_electrometer',
            name='to_date',
        ),
        migrations.RemoveField(
            model_name='svj',
            name='to_date',
        ),
        migrations.AddField(
            model_name='chairman',
            name='status',
            field=models.CharField(choices=[('Aktivní', 'Aktivní'), ('Pozastavené', 'Pozastavené'), ('Neaktivní', 'Neaktivní')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.CharField(choices=[('Aktivní', 'Aktivní'), ('Pozastavené', 'Pozastavené'), ('Neaktivní', 'Neaktivní')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='status',
            field=models.CharField(choices=[('Aktivní', 'Aktivní'), ('Pozastavené', 'Pozastavené'), ('Neaktivní', 'Neaktivní')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='gsm_modul',
            name='status',
            field=models.CharField(choices=[('Aktivní', 'Aktivní'), ('Pozastavené', 'Pozastavené'), ('Neaktivní', 'Neaktivní')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='historicalchairman',
            name='status',
            field=models.CharField(choices=[('Aktivní', 'Aktivní'), ('Pozastavené', 'Pozastavené'), ('Neaktivní', 'Neaktivní')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='historicalcustomer',
            name='status',
            field=models.CharField(choices=[('Aktivní', 'Aktivní'), ('Pozastavené', 'Pozastavené'), ('Neaktivní', 'Neaktivní')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='historicalflat',
            name='status',
            field=models.CharField(choices=[('Aktivní', 'Aktivní'), ('Pozastavené', 'Pozastavené'), ('Neaktivní', 'Neaktivní')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='historicalgsm_modul',
            name='status',
            field=models.CharField(choices=[('Aktivní', 'Aktivní'), ('Pozastavené', 'Pozastavené'), ('Neaktivní', 'Neaktivní')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='historicalmain_electrometer',
            name='status',
            field=models.CharField(choices=[('Aktivní', 'Aktivní'), ('Pozastavené', 'Pozastavené'), ('Neaktivní', 'Neaktivní')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='historicalsub_chairman',
            name='status',
            field=models.CharField(choices=[('Aktivní', 'Aktivní'), ('Pozastavené', 'Pozastavené'), ('Neaktivní', 'Neaktivní')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='historicalsvj',
            name='status',
            field=models.CharField(choices=[('Aktivní', 'Aktivní'), ('Pozastavené', 'Pozastavené'), ('Neaktivní', 'Neaktivní')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='main_electrometer',
            name='status',
            field=models.CharField(choices=[('Aktivní', 'Aktivní'), ('Pozastavené', 'Pozastavené'), ('Neaktivní', 'Neaktivní')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='sub_chairman',
            name='status',
            field=models.CharField(choices=[('Aktivní', 'Aktivní'), ('Pozastavené', 'Pozastavené'), ('Neaktivní', 'Neaktivní')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='sub_electrometer',
            name='status',
            field=models.CharField(choices=[('Aktivní', 'Aktivní'), ('Pozastavené', 'Pozastavené'), ('Neaktivní', 'Neaktivní')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='svj',
            name='status',
            field=models.CharField(choices=[('Aktivní', 'Aktivní'), ('Pozastavené', 'Pozastavené'), ('Neaktivní', 'Neaktivní')], max_length=150, null=True),
        ),
        migrations.RemoveField(
            model_name='customer',
            name='svj',
        ),
        migrations.AddField(
            model_name='customer',
            name='svj',
            field=models.ManyToManyField(to='elektromer_app.svj'),
        ),
    ]
