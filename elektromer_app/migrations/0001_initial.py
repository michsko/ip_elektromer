# Generated by Django 4.2.6 on 2023-10-18 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=244)),
                ('address_street', models.CharField(max_length=255)),
                ('address_orientation_number', models.IntegerField()),
                ('address_number_subscription', models.IntegerField()),
                ('address_city', models.CharField(max_length=255)),
                ('address_postal_code', models.IntegerField()),
                ('contract_number', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gsm_modul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_number', models.CharField(max_length=255)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Svj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_number', models.CharField(max_length=255)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('address_street', models.CharField(max_length=255)),
                ('address_orientation_number', models.IntegerField()),
                ('address_number_subscription', models.IntegerField()),
                ('address_city', models.CharField(max_length=255)),
                ('address_postal_code', models.IntegerField()),
                ('account_number', models.CharField(max_length=255)),
                ('energy_supply', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_electrometer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_number', models.CharField(max_length=255)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True)),
                ('flat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='elektromer_app.flat')),
                ('svj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='elektromer_app.svj')),
            ],
        ),
        migrations.CreateModel(
            name='Solar_electrometer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_number', models.CharField(max_length=255)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True)),
                ('gsm_modul', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='elektromer_app.gsm_modul')),
                ('svj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='elektromer_app.svj')),
            ],
        ),
        migrations.CreateModel(
            name='Main_elektrometer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_number', models.CharField(max_length=255)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('svj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='elektromer_app.svj')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalSvj',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('identification_number', models.CharField(max_length=255)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True)),
                ('date_created', models.DateTimeField(blank=True, editable=False)),
                ('name', models.CharField(max_length=255)),
                ('address_street', models.CharField(max_length=255)),
                ('address_orientation_number', models.IntegerField()),
                ('address_number_subscription', models.IntegerField()),
                ('address_city', models.CharField(max_length=255)),
                ('address_postal_code', models.IntegerField()),
                ('account_number', models.CharField(max_length=255)),
                ('energy_supply', models.CharField(max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical svj',
                'verbose_name_plural': 'historical svjs',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSolar_electrometer',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('identification_number', models.CharField(max_length=255)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('gsm_modul', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='elektromer_app.gsm_modul')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('svj', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='elektromer_app.svj')),
            ],
            options={
                'verbose_name': 'historical solar_electrometer',
                'verbose_name_plural': 'historical solar_electrometers',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMain_elektrometer',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('identification_number', models.CharField(max_length=255)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True)),
                ('date_created', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('svj', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='elektromer_app.svj')),
            ],
            options={
                'verbose_name': 'historical main_elektrometer',
                'verbose_name_plural': 'historical main_elektrometers',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalGsm_modul',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('identification_number', models.CharField(max_length=255)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True)),
                ('date_created', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('svj', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='elektromer_app.svj')),
            ],
            options={
                'verbose_name': 'historical gsm_modul',
                'verbose_name_plural': 'historical gsm_moduls',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFlat',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True)),
                ('date_created', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('gsm_modul', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='elektromer_app.gsm_modul')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('svj', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='elektromer_app.svj')),
            ],
            options={
                'verbose_name': 'historical flat',
                'verbose_name_plural': 'historical flats',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCustomer',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=244)),
                ('address_street', models.CharField(max_length=255)),
                ('address_orientation_number', models.IntegerField()),
                ('address_number_subscription', models.IntegerField()),
                ('address_city', models.CharField(max_length=255)),
                ('address_postal_code', models.IntegerField()),
                ('contract_number', models.CharField(max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('svj', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='elektromer_app.svj')),
            ],
            options={
                'verbose_name': 'historical customer',
                'verbose_name_plural': 'historical customers',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalChairman',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('date_created', models.DateTimeField(blank=True, editable=False)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('customer', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='elektromer_app.customer')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('svj', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='elektromer_app.svj')),
            ],
            options={
                'verbose_name': 'historical chairman',
                'verbose_name_plural': 'historical chairmans',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Historicalbalance_sub',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('identification_number', models.CharField(max_length=255)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=8)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('sub_electrometer', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='elektromer_app.sub_electrometer')),
            ],
            options={
                'verbose_name': 'historical balance_sub',
                'verbose_name_plural': 'historical balance_subs',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Historicalbalance_main',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('identification_number', models.CharField(max_length=255)),
                ('balance', models.DecimalField(decimal_places=3, max_digits=10)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('main_elektromer', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='elektromer_app.main_elektrometer')),
            ],
            options={
                'verbose_name': 'historical balance_main',
                'verbose_name_plural': 'historical balance_mains',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='gsm_modul',
            name='svj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='elektromer_app.svj'),
        ),
        migrations.AddField(
            model_name='flat',
            name='gsm_modul',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='elektromer_app.gsm_modul'),
        ),
        migrations.AddField(
            model_name='flat',
            name='svj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='elektromer_app.svj'),
        ),
        migrations.AddField(
            model_name='customer',
            name='svj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='elektromer_app.svj'),
        ),
        migrations.CreateModel(
            name='Chairman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='elektromer_app.customer')),
                ('svj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='elektromer_app.svj')),
            ],
        ),
        migrations.CreateModel(
            name='balance_sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_number', models.CharField(max_length=255)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=8)),
                ('sub_electrometer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='elektromer_app.sub_electrometer')),
            ],
        ),
        migrations.CreateModel(
            name='balance_main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_number', models.CharField(max_length=255)),
                ('balance', models.DecimalField(decimal_places=3, max_digits=10)),
                ('main_elektromer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='elektromer_app.main_elektrometer')),
            ],
        ),
    ]