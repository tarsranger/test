# Generated by Django 5.0.8 on 2024-08-07 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateField(db_index=True)),
                ('checkout', models.DateField()),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flats.flat')),
            ],
            options={
                'indexes': [models.Index(models.F('flat'), models.F('checkin'), name='flat_checkin_idx')],
            },
        ),
    ]
