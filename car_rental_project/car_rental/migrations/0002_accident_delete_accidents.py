# Generated by Django 4.1.2 on 2022-11-14 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_rental', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=500)),
                ('rental', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_rental.rental')),
            ],
        ),
        migrations.DeleteModel(
            name='Accidents',
        ),
    ]
