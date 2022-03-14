# Generated by Django 3.2.12 on 2022-03-13 19:50

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('siteinfo', '0009_auto_20220313_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='field_engineer',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='cluster_name', chained_model_field='cluster_name', null=True, on_delete=django.db.models.deletion.CASCADE, to='siteinfo.cluster'),
        ),
    ]
