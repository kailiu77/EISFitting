# Generated by Django 2.1.7 on 2019-05-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EIS', '0003_automaticactivesample_sample_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='InverseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logdir', models.CharField(max_length=100)),
                ('kernel_size', models.IntegerField(default=7)),
                ('conv_filters', models.IntegerField(default=16)),
                ('num_conv', models.IntegerField(default=2)),
            ],
        ),
    ]
