# Generated by Django 4.0.4 on 2022-04-29 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AaPort',
            fields=[
                ('port', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'aa_port',
                'managed': False,
            },
        ),
    ]
