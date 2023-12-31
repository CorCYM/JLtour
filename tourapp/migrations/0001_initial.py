# Generated by Django 4.0.1 on 2023-03-29 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('location', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('citynumber', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('address', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('attraction', models.CharField(max_length=200, null=True)),
                ('food', models.CharField(max_length=200, null=True)),
                ('path_tour', models.CharField(max_length=200, null=True)),
                ('path_food', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'detail',
                'managed': False,
            },
        ),
    ]
