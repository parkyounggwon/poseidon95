# Generated by Django 4.0.4 on 2022-05-26 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0002_aacargo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AaOrder',
            fields=[
                ('order_cargo', models.CharField(max_length=100)),
                ('order_quantity', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('order_loading_area', models.CharField(blank=True, max_length=100, null=True)),
                ('order_discharging_area', models.CharField(blank=True, max_length=100, null=True)),
                ('order_laydate', models.DateField(blank=True, null=True)),
                ('order_candate', models.DateField(blank=True, null=True)),
                ('order_comm', models.FloatField(blank=True, null=True)),
                ('order_broker', models.CharField(blank=True, max_length=100, null=True)),
                ('order_indate', models.DateField(blank=True, null=True)),
                ('order_charterers', models.CharField(blank=True, max_length=100, null=True)),
                ('order_seq', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'aa_order',
                'managed': False,
            },
        ),
    ]
