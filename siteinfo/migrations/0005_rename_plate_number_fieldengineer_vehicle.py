# Generated by Django 3.2.12 on 2022-03-16 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteinfo', '0004_auto_20220316_0746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fieldengineer',
            old_name='plate_number',
            new_name='vehicle',
        ),
    ]