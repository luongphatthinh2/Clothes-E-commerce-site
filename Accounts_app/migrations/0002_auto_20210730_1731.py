# Generated by Django 3.2.5 on 2021-07-30 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='date_joind',
            new_name='date_joined',
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
