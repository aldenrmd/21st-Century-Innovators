# Generated by Django 4.0.3 on 2022-04-12 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_first_name', models.CharField(max_length=50)),
                ('receiver_last_name', models.CharField(max_length=50)),
                ('receiver_number', models.CharField(max_length=15)),
                ('receiver_email', models.EmailField(max_length=100)),
                ('receiver_address', models.CharField(max_length=100)),
                ('receiver_state', models.CharField(max_length=100)),
                ('receiver_zip', models.CharField(max_length=15)),
                ('receiver_city', models.CharField(max_length=100)),
                ('receiver_country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_first_name', models.CharField(max_length=50)),
                ('sender_last_name', models.CharField(max_length=50)),
                ('sender_number', models.CharField(max_length=15)),
                ('sender_email', models.EmailField(max_length=100)),
                ('sender_address', models.CharField(max_length=100)),
                ('sender_state', models.CharField(max_length=100)),
                ('sender_zip', models.CharField(max_length=15)),
                ('sender_city', models.CharField(max_length=100)),
                ('sender_country', models.CharField(max_length=100)),
            ],
        ),
    ]
