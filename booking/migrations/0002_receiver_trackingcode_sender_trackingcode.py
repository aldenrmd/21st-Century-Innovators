# Generated by Django 4.0.3 on 2022-05-10 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiver',
            name='trackingcode',
            field=models.CharField(default='0000', max_length=100),
        ),
        migrations.AddField(
            model_name='sender',
            name='trackingcode',
            field=models.CharField(default='0000', max_length=100),
        ),
    ]
