# Generated by Django 3.0.7 on 2020-06-05 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=16, verbose_name='Vehicle Registration Number')),
                ('color', models.CharField(max_length=128)),
                ('model', models.CharField(max_length=64)),
                ('brand', models.CharField(choices=[('HN', 'HONDA'), ('TY', 'Toyota'), ('MD', 'Mercedes'), ('BMW', 'BMW')], max_length=16)),
                ('image', models.ImageField(upload_to='media/', verbose_name='Vehicle Image')),
                ('menufectured_date', models.DateField(auto_now_add=True, verbose_name='Menufectured Date')),
            ],
        ),
    ]
