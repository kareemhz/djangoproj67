# Generated by Django 2.2.5 on 2019-09-28 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('userid', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=2)),
                ('pincode', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=6)),
                ('en', models.CharField(max_length=2)),
                ('nonen', models.CharField(max_length=5)),
                ('about', models.CharField(max_length=100)),
            ],
        ),
    ]
