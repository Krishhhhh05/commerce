# Generated by Django 3.1.5 on 2021-01-29 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210127_2323'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-time',)},
        ),
    ]
