# Generated by Django 3.1.2 on 2020-10-20 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_date', models.DateField(verbose_name='Appointment Date')),
                ('app_slot', models.PositiveIntegerField()),
                ('phone', models.CharField(max_length=11)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.services')),
            ],
        ),
    ]