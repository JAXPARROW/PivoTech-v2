# Generated by Django 3.2.12 on 2022-03-13 21:59

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('siteinfo', '0023_alter_site_field_engineer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='field_engineer',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='cluster', chained_model_field='cluster', null=True, on_delete=django.db.models.deletion.CASCADE, show_all=True, to='siteinfo.cluster'),
        ),
    ]
