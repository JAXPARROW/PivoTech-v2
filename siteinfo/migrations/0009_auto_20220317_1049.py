# Generated by Django 3.2.12 on 2022-03-17 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteinfo', '0008_auto_20220317_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='htt_class',
            field=models.CharField(choices=[('B', 'B'), ('C', 'C')], default='C', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='power_type',
            field=models.CharField(blank=True, choices=[('AC', 'AC'), ('DC', 'DC')], default='DC', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='DG_type',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='MKII_PLC',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=50),
        ),
        migrations.AlterField(
            model_name='site',
            name='PLC_locked',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=50),
        ),
        migrations.AlterField(
            model_name='site',
            name='QSV',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='SPA_Status',
            field=models.CharField(blank=True, choices=[('Configured', 'Configured'), ('Non-Configured', 'Non-Configgured'), ('Optimized', 'Optimized')], default='Optimized', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='access_restricted',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='configuration',
            field=models.CharField(choices=[('GHS', 'GHS'), ('GHX', 'GHX'), ('GXX', 'GXX'), ('OHS', 'OHS'), ('OHX', 'OHX'), ('OXX', 'OXX')], default='GXX', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='criticality',
            field=models.CharField(choices=[('C1', 'C1'), ('C2', 'C2')], default='C1', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='dg_ownership',
            field=models.CharField(choices=[('HTT-DG', 'HTT-DG'), ('LL-DG', 'LL-DG'), ('NON-DG', 'NON-DG')], default='HTT-DG', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='dg_present',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='fuel_cph',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
        migrations.AlterField(
            model_name='site',
            name='grid_status',
            field=models.CharField(choices=[('Off Grid', 'Off Grid'), ('Grid', 'Grid')], default='Grid', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='luku_cph',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
        migrations.AlterField(
            model_name='site',
            name='luku_payment',
            field=models.CharField(choices=[('Post-Paid', 'Post-Paid'), ('Pre-Paid', 'Pre-Paid'), ('Off-Grid', 'Off-Grid'), ('LandLord', 'LandLord'), ('Consolidated', 'Consolidated')], default='Pre-Paid', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='region',
            field=models.CharField(choices=[('Dar es salaam', 'Dar es salaam'), ('Tanga', 'Tanga'), ('Pwani', 'Pwani'), ('Lindi', 'Lindi'), ('Mtwara', 'Mtwara'), ('Ruvuma', 'Ruvuma'), ('Morogoro', 'Morogoro')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='restriction_reasons',
            field=models.CharField(blank=True, choices=[('Safety Reasons', 'Safety Reasons'), ('Permit Reasons', 'Permit Reasons'), ('No Restriction', 'No Restriction')], default='No Restriction', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_class',
            field=models.CharField(choices=[('Platinum', 'Platinum'), ('Gold', 'Gold'), ('Silver', 'Silver')], default='Silver', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_status',
            field=models.CharField(choices=[('On Air', 'On Air'), ('Decomisioned', 'Decomisioned')], default='Online', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_type',
            field=models.CharField(choices=[('IBS', 'IBS'), ('Roof Top', 'Roof Top'), ('Green Field', 'Green Field')], default='Green Field', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='tanesco_region',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
