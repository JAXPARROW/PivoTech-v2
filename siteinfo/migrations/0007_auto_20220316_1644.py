# Generated by Django 3.2.12 on 2022-03-16 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteinfo', '0006_auto_20220316_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='MKII_PLC',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=3),
        ),
        migrations.AlterField(
            model_name='site',
            name='PLC_locked',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=3),
        ),
        migrations.AlterField(
            model_name='site',
            name='access_restricted',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='configuration',
            field=models.CharField(choices=[('GHS', 'GHS'), ('GHX', 'GHX'), ('GXX', 'GXX'), ('OHS', 'OHS'), ('OHX', 'OHX'), ('OXX', 'OXX')], default='GXX', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='criticality',
            field=models.CharField(choices=[('C1', 'C1'), ('C2', 'C2')], default='C1', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='dg_ownership',
            field=models.CharField(choices=[('HTT-DG', 'HTT-DG'), ('LL-DG', 'LL-DG'), ('NON-DG', 'NON-DG')], default='HTT-DG', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='dg_present',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='grid_status',
            field=models.CharField(choices=[('Off Grid', 'Off Grid'), ('Grid', 'Grid')], default='Grid', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='luku_payment',
            field=models.CharField(choices=[('Post-Paid', 'Post-Paid'), ('Pre-Paid', 'Pre-Paid'), ('Off-Grid', 'Off-Grid'), ('LandLord', 'LandLord'), ('Consolidated', 'Consolidated')], default='Pre-Paid', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_class',
            field=models.CharField(choices=[('Platinum', 'Platinum'), ('Gold', 'Gold'), ('Silver', 'Silver')], default='Silver', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_status',
            field=models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], default='Online', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_type',
            field=models.CharField(choices=[('IBS', 'IBS'), ('Roof Top', 'Roof Top'), ('Green Field', 'Green Field')], default='Green Field', max_length=30, null=True),
        ),
    ]
