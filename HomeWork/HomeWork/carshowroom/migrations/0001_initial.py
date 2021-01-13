# Generated by Django 3.1.5 on 2021-01-13 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Car_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(max_length=1000)),
                ('price', models.IntegerField(max_length=100000)),
                ('description', models.CharField(max_length=1000)),
                ('dealer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carshowroom.dealer')),
            ],
        ),
    ]
