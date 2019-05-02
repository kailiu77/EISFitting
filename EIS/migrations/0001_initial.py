# Generated by Django 2.1.7 on 2019-05-02 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EISSpectrum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=1000, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('dataset', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='EIS.Dataset')),
            ],
        ),
        migrations.CreateModel(
            name='ImpedanceSample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_ang_freq', models.FloatField()),
                ('real_part', models.FloatField()),
                ('imag_part', models.FloatField()),
                ('active', models.BooleanField(default=True)),
                ('spectrum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EIS.EISSpectrum')),
            ],
        ),
    ]
